'''

给你一个二维列表：找到每一个小列表的最小值

while 条件：

1 终止条件

2 前进条件
'''
def findMin(list):
    p = []
    for i in range(len(list)):
        temp = list[i][0]

        for j in range(len(list[i])):

            if list[i][j] < temp:
                temp = list[i][j]


        p.append(temp)

    return p

def minNum(numList):
    result = numList[0]
    for i in range(len(numList)):
        if numList[i] < result:
            result = numList[i]
    return result


def finMin2(doublelist):
    p = []
    for i in range(len(doublelist)):
        temp = minNum(doublelist[i])
        p.append(temp)

    return p


def qiuZhi(doubielist):
    p = []
    for i in range(len(doubielist)):
        he = 0
        j = 0

        while he < 3:
            he = he + doubielist[i][j]
            j =j + 1
        p.append(he)
    return p

def simpleHe(numlist):


    i = 0
    he = 0
    while he < 3:
        he = he + numlist[i]
        i = i + 1
    return he
def qiuZhi2(doubieList):
    p = []
    for i in range(len(doubieList)):
        temp = simpleHe(doubieList[i])
        p.append(temp)
    return p




if __name__ == '__main__':
    double = [[1, 2, 3], [2, 3, 5, 1], [7, 8, 94, 5]]
    a = qiuZhi2(double)
    print(a)