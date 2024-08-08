import pandas as pd
import numpy as np

from sklearn import linear_model 
from sklearn.metrics import mean_squared_error,r2_score

import matplotlib.pyplot as plt
if __name__ == '__main__':
    acci = pd.read_csv("D:/ProgramData/pythonProject/1030次世代交通/train.csv")
    acci = acci.dropna()

    # print("可选择的特征有PassengerId Survived Pclass Age SibSp Parch Fare Embarked")
    feature = str(input("请输入你想用什么特征对Fare进行预测:\n"))

    acci_X = acci[[feature]]
    acci_y = acci["Fare"]

    # print(acci_X.dtypes)
    # print(acci_y.dtypes)
    # print(acci_X)
    acci_X_train = acci_X[:-20]
    acci_X_test = acci_X[-20:]
    acci_y_train = acci_y[:-20]
    acci_y_test = acci_y[-20:]

    regr = linear_model.LinearRegression()

    regr.fit(acci_X_train, acci_y_train)

    acci_y_pred = regr.predict(acci_X_test)

    print("回归模型系数为:\n", regr.coef_)
    print("均方误差为: %.2f" % mean_squared_error(acci_y_test, acci_y_pred))
    print("决定系数为: %.2f" % r2_score(acci_y_test,acci_y_pred))

    plt.figure()
    plt.scatter(acci_X_test, acci_y_test, color = "black")
    plt.plot(acci_X_test, acci_y_pred, color = "blue", linewidth = 3)
    plt.xticks(())
    plt.yticks(())
    plt.show()








