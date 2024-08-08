# 默认列表中有超过列表一半个数的数
# 竞赛格式
num2 = input()
list2 =[int(i) for i in num2.split()]
list2 = sorted(list2)
num = list2[len(list2)//2]  # 偶数个时中间数为整数，所真正取得数为中间数+1
print(num)