import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

import numpy as np
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


if __name__ == '__main__':
    acci = pd.read_csv("D:/ProgramData/pythonProject/1030次世代交通/train.csv")
    acci = acci.dropna()

    feature = str(input("请输入你想用什么特征对Fare进行预测:\n"))

    acci_X = acci[feature]
    acci_y = acci["Survived"]

    print(acci_X)
    print(acci_y)
    
    acci_X_train = acci_X[:-20]
    acci_X_test = acci_X[-20:]
    acci_y_train = acci_y[:-20]
    acci_y_test = acci_y[-20:]

    model = DecisionTreeClassifier(max_depth=2)
    model.fit(acci_X_train, acci_y_train)

    acci_y_pred1 = model.predict(acci_X_test)

    accuracy = accuracy_score(acci_y_test, acci_y_pred1)

    print("准确性 (Accuracy): {:.2f}%".format(accuracy * 100))

    plt.figure(figsize=(12, 6))
   
    plot_tree(model, filled=True, feature_names=[feature], class_names=["Survived"])
    plt.show()
    plt.legend()
    plt.show()
