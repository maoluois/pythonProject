'''
while 循环
123456

while === for + if + break

break 终止当前循环
continue 提前执行
'''

def he(num1):
    i = 0
    num = 0
    while num <= num1:
        i = i + 1
        num += i
          #判断跳出的时候


    return i,num


#如果遇到一个大于10的值的时候，停止，告诉我是第几个
def findNum(doublelist,number1):
    p = []
    for i in range(len(doublelist)):
        k = 0
        while doublelist[i][k] <= number1:
            k = k + 1
        p.append(k)
    return p

'''

造一个乘法口诀表
1*1 。。。1*9
2*2.。。。2*9

'''


#
# def multi():
#   for i in range(1,10):
#       for j in range(1,10):
#           if i > j:
#               continue
#
#           print(str(i)+'*'+str(j))

# def multi1():
#     for i in range(1,10):
#         for j in range(1,10):
#             if j >= i:
#                 print(str(i)+'*'+str(j))

def mult():
    for i in range(1,10):
        for j in range(i,10):

            print(str(i)+'*'+str(j)+'='+str(j*i))

def multi2():
    for i in range(1,10):
        for j in range(1,i+1):

            print(str(j)+'*'+str(i)+'='+str(i*j),end=' ') #print里面默认换行，打印一次换一行
        #
        print()
if __name__ == '__main__':

    # a,b = he(2000)
    # print(a,b)
    # double = [[1, 2, 3, 9, 12], [2, 3, 5, 23], [7, 8, 56, 94, 5]]
    # a = findNum(double,10)
    # print(a)
    multi2()
