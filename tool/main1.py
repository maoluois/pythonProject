
def squre(x):
    return x**2

if __name__ == '__main__':

    # a = [1,4,6,2,18]
    # print(max(a))
    # print(min(a))
    # print(sum(a))
    #
    # b = sorted(a)
    #
    # c = sorted(a,reverse=True)
    # print(c)
    #
    # print(a)
    #
    # d = list(reversed(a))
    # print(d)

    # 映射，集体操作
    '''
    map(function,可携带对象(列表，元组，字典))
    
    function 某一种操作
    
    
    '''

    # a = input().split()
    # print(a)

    # a = [int(i) for i in a]
    # print(a)
    # 匿名函数的方式：在map里面写函数
    a = [1,2,3,4]
    c = [2,3,4,5]

    m = list(map(lambda x,y:x+y,a,c))
    b = list(map(lambda x:x+1,a))
    print(m)