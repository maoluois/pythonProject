import pandas as pd
data = [[1, 4], [2, 5], [3, 6]]

# for item in data:
#     print(item[1])
# df = pd.DataFrame(data,index=['row1','row2','row3'],columns=['col1','col2'])
# print(df)
states = ["California", "Texas", "Florida", "New York"]
population = [39613493, 29730311, 21944577, 19299981]

# 用字典保存
dict_data = {"Status":states,"Population":population}
df = pd.DataFrame(dict_data)
print(df)