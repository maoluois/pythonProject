'''

map
12345


'''
def add(x):
    return x+1

if __name__ == '__main__':

    # a = input().split()
    # print(a)
    # a = list(map(int,a))
    #
    # print(a)
    #
    # c = list(map(add,a))
    # print(c) #下一行类似
    #
    # b = list(map(lambda x:x+1 ,a))
    # print(b)
    a = [1,2,3,4]
    b = [3,4,5,6]
    m = [[1,2,3],[4,5,6],[7,8,9]]

    c = list(map(lambda x,y:x*y,a,b))
    print(c)

    d = list(map(lambda x:max(x),m))