import sys
# 俩个单词组成，第二个单词开头要大写
def sumList(num_list):
    sum_num = 0
    for num in num_list:
        sum_num = sum_num + num
    return sum_num

'''
迭代器和生成器




'''
def gen(N):         # 跟直接return有怎样的区别
    # 有什么好处
    for i in range(N):
        yield i**2

def makeDeal(a):
    a += 9
    return a



if __name__ == '__main__':
    # a = 5
    # makeDeal(a) 没有给予一个东西承接
    # print(a)  只能输出5

    # a = [1,2,3,4,5]
    # it = iter(a)
    # sum_num = sumList(a)
    # print(sum_num)
    # while 1:
    #     try:
    #         print(next(it))
    #     except:
    #         sys.exit()
    # for i in gen(5):
    #     print(i)

    # b = [ i**2 for i in range(5)]
    # print(b)

    # c = [i for i in range(51)]
    # print(c)
    #
    # d = [i for i in range(3,10)]
    # print(d)
    #

    m = [1,2,6,3,2,7]
    m.sort()
    print(m)

    for i in range(len(m) - 1): #控制找几次最大值
        # 5
        for j in range(len(m) - 1 - i):
            if m[j] > m[j + 1]:
                temp = m[j]
                m[j] = m[j + 1]
                m[j + 1] = temp
#                 sort的原理




































