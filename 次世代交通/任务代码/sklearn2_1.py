import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

if __name__ == '__main__':
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.metrics import accuracy_score

    acci = pd.read_csv("D:/ProgramData/pythonProject/1030次世代交通/train.csv")
    acci = acci.dropna()

    feature = str(input("请输入你想用什么特征对Fare进行预测:\n"))

    acci_X = acci[[feature]]
    acci_y = acci["Survived"]
    
    acci_X_train = acci_X[:-20]
    acci_X_test = acci_X[-20:]
    acci_y_train = acci_y[:-20]
    acci_y_test = acci_y[-20:]

    regr_1 = DecisionTreeRegressor(max_depth=2)
    regr_1.fit(acci_X_train, acci_y_train)

    acci_y_pred1 = regr_1.predict(acci_X_test)

    threshold = 0.5
    acci_y_pred1 = [1 if x >= threshold else 0 for x in acci_y_pred1]

    accuracy1 = accuracy_score(acci_y_test, acci_y_pred1)

    print("准确性 (Accuracy): {:.2f}%".format(accuracy1 * 100))

    plt.figure()
    plt.scatter(acci_X_train, acci_y_train, s=20, edgecolors="black", c="darkorange", label= "data")
    plt.plot(acci_X_test, acci_y_pred1, color="cornflowerblue", label="max_depth=2", linewidth=2)

    plt.xlabel("data")
    plt.ylabel("target")
    plt.title("Decision Tree Regression")
    plt.text(2, 0.8, "准确性: {:.2f}%".format(accuracy1 * 100), fontsize=12, color="red")

    plt.legend()
    plt.show()


