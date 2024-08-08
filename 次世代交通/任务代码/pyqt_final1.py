import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QInputDialog, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QMessageBox

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

class DataManipulationApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("事故数据分析和预测程序（第一版）")
        self.setGeometry(100, 100, 600, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout() # 建立一个垂直布局对象

        self.import_button = QPushButton("导入数据(.csv 或 .xlsx)", self)
        self.label_feature_button = QPushButton("输入标签和特征", self)
        self.split_button = QPushButton("数据分割", self)
        self.train_button = QPushButton("模型训练", self)
        self.predict_button = QPushButton("进行预测", self)

        self.import_button.clicked.connect(self.import_data)
        self.label_feature_button.clicked.connect(self.input_labels_features)
        self.split_button.clicked.connect(self.split_data)
        self.train_button.clicked.connect(self.train_model)
        self.predict_button.clicked.connect(self.predict)
        

        self.layout.addWidget(self.import_button)
        self.layout.addWidget(self.label_feature_button)
        self.layout.addWidget(self.split_button)
        self.layout.addWidget(self.train_button)
        self.layout.addWidget(self.predict_button)
        

        self.central_widget.setLayout(self.layout)

        self.acci = None  # 初始化所需变量
        self.acci_X = None
        self.acci_y = None
        self.acci_X_train = None
        self.acci_X_test = None
        self.acci_y_train = None
        self.acci_y_test = None
        self.model = None

    def import_data(self):
        options = QFileDialog.Options() # 创建一个文件对话框选项对象，用于配置文件对话框的行为
        file_name, _ = QFileDialog.getOpenFileName(self, "导入数据文件", "", "All Files (*);;CSV Files (*.csv);;Excel Files (*.xlsx)", options=options)
        # _ 为占位符，用于接收文件过滤器
        if file_name:
            try:
                if file_name.endswith(".csv"):
                    self.acci = pd.read_csv(file_name)
                    self.acci = self.acci.dropna()
                elif file_name.endswith(".xlsx"):
                    self.acci = pd.read_excel(file_name)
                    self.acci = self.acci.dropna()
                QMessageBox.information(self, "数据已导入", "数据已成功导入。")
            except Exception as e:
                QMessageBox.critical(self, "错误", f"导入数据时出错: {str(e)}")

    def input_labels_features(self):
        if self.acci is not None:
            allowed_labels = ["Survived", "Pclass", "Sex", "SibSp", "Parch", "Embarked"]  # 允许的标签列表
            allowed_features = ["Age", "Fare", "Survived", "Pclass", "Sex", "SibSp", "Parch", "Embarked"]

            # 打开对话框以输入标签和特征
            label, ok = QInputDialog.getText(self, "输入标签", "从以下标签中挑选并输入标签(Survived, Pclass, Sex, SibSp, Parch, Embarked):")

            if ok:
                feature, ok = QInputDialog.getText(self, "输入特征", "从以下特征中挑选并输入特征(Age, Fare, Survived, Pclass, Sex, SibSp, Parch, Embarked):")
                if ok:
                    if label in allowed_labels and feature in allowed_features:
                        self.acci_X = self.acci[[feature]]
                        self.acci_y = self.acci[[label]]
                        
                        if feature == "Sex":
                            for i in range(len(self.acci_X)):
                                if str(self.acci_X.iloc[i, 0]) == "female":
                                    self.acci_X.iat[i, 0] = 0
                                else:
                                    self.acci_X.iat[i, 0] = 1
                        elif feature == "Embarked":
                            for i in range(len(self.acci_X)):
                                if str(self.acci_X.iloc[i, 0]) == "C":  # .iat 主要用于在需要快速访问单个元素时，提供比使用 .iloc 更高的性能，
                                    self.acci_X.iat[i, 0] = 0           # 因为它不需要执行切片操作。但请注意，它适用于单个元素的访问，
                                                                        # 如果需要获取多个元素或切片数据，仍然建议使用 .iloc
                                elif str(self.acci_X.iloc[i, 0]) == "S":
                                    self.acci_X.iat[i, 0] = 1
                                else:
                                    self.acci_X.iat[i, 0] = 2                              
                                    
                        
                        QMessageBox.information(self, "标签和特征", f"已选择标签: {label}\n已选择特征: {feature}")
                    elif label not in allowed_labels:
                        QMessageBox.critical(self, "错误, 无效的标签", "标签不在允许的列表中。")
                    elif feature not in allowed_features:
                        QMessageBox.critical(self, "错误, 无效的特征", "特征不在允许的列表中.")

            else:
                QMessageBox.critical(self, "错误, 没有数据", "请在选择特征和标签之前导入数据。")


    def split_data(self):
        if self.acci_X is not None and self.acci_y is not None:
        # 打开对话框以输入测试集比例
            ratio, ok = QInputDialog.getDouble(self, "数据分割", "请输入测试集比例 (0.0 到 1.0):", 0.3, 0.0, 1.0, 2)
            if ok:
                split_index = int(len(self.acci_X) * ratio)
                self.acci_X_train = self.acci_X.iloc[:-split_index]
                self.acci_X_test = self.acci_X.iloc[-split_index:]
                self.acci_y_train = self.acci_y.iloc[:-split_index]
                self.acci_y_test = self.acci_y.iloc[-split_index:]
                QMessageBox.information(self, "数据已分割", f"数据已按 {ratio:.1%} 比例分割为训练集和测试集。") 
            else:
                QMessageBox.critical(self, "错误", "请输入范围内正确格式的字符")

        else:
            QMessageBox.critical(self, "错误", "没有数据, 请在分割之前导入数据。")


    def train_model(self):
        if self.acci_X_train is not None and self.acci_y_train is not None:
            self.model = DecisionTreeClassifier(max_depth=3)
            self.model.fit(self.acci_X_train, self.acci_y_train)

            QMessageBox.information(self, "模型训练", "模型已经训练完成。")
        else:
            QMessageBox.critical(self, "错误", "没有数据可供训练, 请先分割数据。")

    def predict(self):
        if self.acci_X_test is not None and self.acci_y_test is not None and self.model is not None:
            self.acci_y_pred = self.model.predict(self.acci_X_test)
            self.accuracy = accuracy_score(self.acci_y_test, self.acci_y_pred)
            QMessageBox.information(self, "预测", "已完成预测。准确性 (Accuracy): {:.2f}%".format(self.accuracy * 100))
        else:
            QMessageBox.critical(self, "错误", "没有测试数据或模型。请先分割数据并训练模型。")

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 命令行参数，用于接受信号指令信息
    window = DataManipulationApp()
    window.show()
    sys.exit(app.exec_())
