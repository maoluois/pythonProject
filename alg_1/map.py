# a = map(int, input().split(" "))
# print(a)
# print(list(a))
# a = iter(a)  
# print(next(a)) 
"""
list 是可迭代对象
迭代器是可迭代对象执行某种操作的机器
next 可以去访问迭代器
"""
list(map(lambda x:x**2, [3, 4, 5, 6]))

b = [2, 6 ,3]
c = [3, 4, 5]

list(map(len, ['white', 'blue', 'green', 'yellow']))



list(map(lambda a, b:a + b, b, c))

# upper()将字母大写
list(map(lambda x: x.upper(), ['white', 'blue', 'green', 'yellow']))

list(map(int, '789'))



dict_1 = {'星期一': '吃榴莲', '星期二': '吃葡萄' , '星期三': '吃西瓜', '星期四': '吃樱桃', '星期五': '吃波罗蜜', '星期六': '吃葡萄', '星期天': '吃猕猴桃'}
list(dict_1.keys())
list(map(str, {'星期一': '吃榴莲', '星期二': '吃葡萄' , '星期三': '吃西瓜', '星期四': '吃樱桃', '星期五': '吃波罗蜜', '星期六': '吃葡萄', '星期天': '吃猕猴桃'}))

"""
1. 函数
2. 可迭代对象,存在多个可访问的东西,可用for循环循环

"""
"""
3
1 2 3 4 5
3 2 1 4 5
6 3 2 1 4

"""
# 竞赛输入
a = input()
hang = int(a)
total_list = []
for i in range(hang):
    total_list.append(list(map(int, input().split(" "))))
print(total_list)