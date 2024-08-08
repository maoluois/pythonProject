'''

字典的应用

元组  （1，2，3） 元组无法更改只支持访问
列表[1,2,3]

函数

集合set()(创建一个集合）:1.，互异性，2，没有固定顺序，确定的
'''


if __name__ == '__main__':
    height = {'小罗':178, '小白':183, '小霍':160}
    a = [1,4,2]
    #
    # b = sorted(a)
    # print(a)
    # print(b)


    c = sorted(height.items(),key=lambda d:d[1])
    # print(c)
    #
    # print(c[0][1])
    #sorted(d.items(), key=lambda x: x[1]) 中 d.items() 为待排序的对象；key=lambda x: x[1] 为对前面的对象中的第二维数据（即value）的值进行排序。 key=lambda  变量：变量[维数] 。维数可以按照自己的需要进行设置。


    jihe = set('asfaasdsfsaf')
    print(jihe)
    jihe.add('g')
    jihe.update(a) # 添加可哈希类型元素 int tup str bool 可拆卸但不可变的
    jihe.remove('a')      # 添加不可哈希元素 list dict set  
    b = jihe.pop()  # 随机（集合无序性）删掉第一个元素并返回
    print(jihe,b)

    if 'f' in jihe:
        print('heiio')


    x = (1,4,6) # 元组 tuple
    print(x)















































