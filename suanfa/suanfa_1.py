
"""
双层循环
for i in range
    for j in range


打印乘法乘法口诀表

1*1
1*2 2*2
1*3 2*3 3*3


求最大公因数
12，15:3
3, 6:3

if num1 > num2:  num1 永远只存小  ，num2 只存大的
    temp = num1
    num1 = num2
    num2 = temp

if num2 % num1 == 0:
    :return num1
else:
    yueeshu = 1
    for i in range(1,num1):
        if num1 % i == 0 and num2 % i == 0
            yueshu = 1



"""
def maxYnum(num1,num2):

    if num1 > num2:
        temp = num1
        num1 = num2
        num2 = temp

    if num2 % num1 == 0:
        return num1
    else:
        yueeshu = 1
        for i in range(1,num1):
            if num1 % i == 0 and num2 % i == 0:
                yueshu = i
        return yueshu




if __name__ == '__main__':
    for i in range(1,10):
        for j in range(1,i+1):
            print("{0}*{1}={2}\t".format(j, i, j*i),end='')
            # format,自动转化格式 换掉{NUM}，\t制表符 空四格
        print()



    # for i in range(5):
    #     print(i, end='\n')#换行

    m = maxYnum(36,48)
    print(m)