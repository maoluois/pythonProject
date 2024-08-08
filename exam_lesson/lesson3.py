# 字典

# 1，找出指定元素
#  {key:value}   key : 字符串，value可以是任何东西
#  [1,2,3,4,5] n, o(n)
#  字典的时间复杂度，查找的话是o(1)

#  {'xiao':93,'luo':95}
# 查找name为a的为分数
if __name__ == '__main__':
    dict_data = {'xiao': 93, 'luo': 95}
    a = 'xiao'
    if a in dict_data:
        print(dict_data[a])
    else:
        print('不存在name为:', a)

# 访问方式
    for i in dict_data:
        print(i)

    for i in dict_data.values():
        print(i)

    for i in dict_data.items():
        print(i)
        print(i[0], i[1])
# sorted 排序
    b = sorted(dict_data.items(), key=lambda x: x[1],reverse=True)
    print(b)

# 元组 和 集合
# [],()
    m = (12, 45, 67)
    for i in m:
        print(i)
# m[1] = 0
    n = [1, 2, 3]
    n[2] = 0
    print(n)

    dict1 = {'name': 'Alice', 'age': 25}
    dict2 = {'gender': 'female', 'age': 26, 'score': 90}

    dict2['name'] = 'Alice'
#     for key in dict1:
#         dict2[key] = dict1[key]
# # 谁合并到谁，原来的值会被替代掉
#     print(dict2)
    dict2.update(dict1)
    print(dict2)
# 集合 :{},set(),dict(),
    a = {1, 2, 3, 45}
# a = set()
    a.add(6)
    print(a)
    a.remove(45)
    print(a)
    list1 = [1, 2, 5, 2, 3, 7, 8, 3, 7, 89, 5, 6]
    # 问这个列表有多少个元素（不一样的）
    # a = set()
    #   for i in list1:
    #       a.add()
    result = set(list1)
    print(result, len(result))

    # 一般是集合，列表，元组可以互相转化
    m = {1, 2, 3, 4}
    n = {3, 4, 5, 6}
    # 交集
    print(m & n)
    # 并集
    print(m | n)
    # 差值
    print(m - n)


# 类
"""
1，需要有明确的对象

2，功能丰富，不仅仅单一的函数，而是非常多的函数组合体
3，统一接口定义，函数配合使用。
"""


class Dog():
    # 初始化函数
    def __init__(self, name, age):
            self.name = name
            self.age = age

    def speak(self):
            print('我的名字是:', self.name)
# 实例化 用变量实现.savedjkjk.save
dog1 = Dog('xiaobai', 5)
dog2 = Dog('xiaohei', 8)

dog1.speak()
dog2.speak()
