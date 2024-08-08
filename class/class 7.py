'''
对双层函数进行操作

1 把所有的小列表的长度输出出来求和

2 输出每个小列表的和

3 嵌套 一个函数调用另一个函数


'''


def makeSum(double):

    sum = 0
    for i in range(len(double)):
        for j in range(len(double[i])):
            sum = sum + double[i][j]
    return sum
def makesum_l(list):

    q = []
    for i in range(len(double)):

        he = 0
        for j in range(len(double[i])):

            he += double[i][j]
        q.append(he)

    return q

def qiuhe(numList):
    he = 0
    for i in range(len(numList)):
        he += numList[i]
    return he


def makeSum3(doubie):
    he = 0
    for i in range(len(double)):
        temp_he = qiuhe(double[i])
        print(temp_he)
        he += temp_he
    return he


if __name__ == '__main__':
    double = [[1, 2, 3], [2, 3, 5, 1], [7, 8, 94, 5]]
    a = makesum_l(double)
    print(a)