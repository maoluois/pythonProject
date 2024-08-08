'''

continue



break




while  (break continue)
一般来说while能用for替代


输出所有下标是基数的1，3，5，7，9

输出100，99.。。。

while 更加灵活
'''

def ture(numList):
    i =0
    while True:
        print(numList[i])
        i += 1
        if i == len(numList):
            break





def ceShi():
    for i in range(5):
        print(i)

        if i == 3:
            break  # 如果满足，后面的语句不执行，结束所以循环
        print('你好')

def cheShi2():
    for i in range(5):
        print(i)

        if i == 3:
            continue  #提前循环
        print('你好')


def checkNumber(doublelist):


    for i in range(len(doublelist)):
        for j in range(len(doublelist[i])):

            if doublelist[i][j] >= 7:
                continue
            print(doublelist[i][j])
            print('你好')

def checkSum(dooublelist,he):

    result = 0
    for i in range(len(dooublelist)):
        sum = 0
        for j in range(len(dooublelist[i])):
            sum += dooublelist[i][j]
        if sum >= he:
            result = sum
            break
    return result

def read(numList):
    a = len(numList)
    i = 0
    while i < a:
        print(numList[i])
        i += 1
#while for 的转化


if __name__ == '__main__':
    # j = 1
    # i = 2
    # print('%d*%d=%d'%(i,j,i*j),end='\t')#简便输出

    # for i in range(5):
    #     print(i)
    #
    #     if i == 3:
    #         continue  #提前循环
    #     print('你好')

    doubieList = [[1,5,3],[3,6,4],[7,3,12],[5,2,8]]

    a = checkSum(doubieList,20)
    print(a)