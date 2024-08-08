'''
1.指定个数 :1.78543 保留俩位小数


'''

if __name__ == '__main__':
    a = 5
    b = 8
    m = 2
    # 如果执行除法，会自动转化成float型
    d = int(b/m)
    g = b // m
    print(d)
    print(g)

    #
    c = a/b
    # d = b/m
    # print(d)
    print(c)
    c = c + 100
    # 指定保留俩位小数
    # 1 % f-float小数
    print('保留俩位小数后为: %.2f' % c)
    print('你好{0}'.format(c))
    print(format(c,'.2f'))  # 将第二位的条件直接带入第一中
    # 会进行五舍六入
    # print(round(c))
    # print(round(c,1))
    # print(round(c,2))













