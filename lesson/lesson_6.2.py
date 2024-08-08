'''

字典：{}

d = {key1 : value1, key2 : value2 }
d = {小明 : 183, 小罗 :178}

d = {小明 : {英语: 100， 数学: 130}小罗 :178}
print【小明】【英语】


m = d['小明']

值可以取任何数据类型，每个人的值可以不一样，但键必须是不可变的。
'''
#函数
def speak():
    print('hello')



if __name__ == '__main__':
    speak()
    
    dict = {'a': 1, 'b': 2, 'c': 3}
    # print(dict['c'])
    #
    # for i in dict:
    #     print(dict[i])
    #     print(i)

    # for i,j in enumerate(dict):
    #     print(i,j)    #下标和键

    # print(dict.items())
    # m = dict.items()
    # print(m)
    # for key,value in dict.items():#只提供访问
    #     print(key,value)
    #
    #
    # print(dict.values())
    # # for i in dict.values():
    #     print(i)

    # print(dict.keys())
    # 访问
    # 建立一个字典
    a = {}
    a['google'] = 1
    a['baidu'] = 2
    a['sina'] = 3
    a['louis_high'] = '178cm'
    #
    print(a)

    # 建立一个字典:  有三个人的名字:键
    # 值包含 : 身高，性别，体重，年龄

    # 查找 年龄是15岁的人，并输出，没有输出没有

    # a.clear()
    del[a['sina']]
    print(a)