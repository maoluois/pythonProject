import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv("D:/ProgramData/pythonProject/小A的任务/田字型散点.csv")
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用SimHei字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
X = data.iloc[0]
Y = data.iloc[1]
# print(len(data))
# z = data.head(3)
# print(len(X))
# print(len(Y))
# print(len(z))
print(X)
print(Y)
# print(z)
color_row = data.iloc[2]
print(color_row)

colors = ['blue' if value == 0 else 'red' for value in color_row]

     

plt.scatter(X, Y, c = colors)

# 将原点移到绘图界面中心
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# 设置坐标轴原点在绘图界面中心
plt.gca().spines['left'].set_position('zero')
plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
# 显示图例
plt.legend(labels=['0: blue', '1: red'])

plt.title("与或散点图")


plt.show()