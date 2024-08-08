'''

 double = [[1, 2, 3, 6], [2, 3, 5, 1], [7, 8, 56, 94, 5]]

输入num1 num2
从num1 * 到num2

[1,2,4,4,6,5,7]

'''

def simpleHe(numlist):


    i = 0
    he = 0
    while he < 10:
        he = he + numlist[i]
        i = i + 1


    return i - 1


def qiuZhi2(doubieList):
    p = []
    for i in range(len(doubieList)):
        temp = simpleHe(doubieList[i])
        p.append(temp)
    return p


def chengJi(num1,num2):
    ji = 1
    for i in range(num1,num2+1):
        ji = ji*i

    return ji
def quChong(numlist):

    a = set()
    for i in numlist:
        a.add(i)
    return a
if __name__ == '__main__':
    double = [[1, 2, 3, 6], [2, 3, 5, 1], [7, 8, 56, 94, 5]]
    l = [1,2,4,4,6,5,7]
    a = quChong(l)
    print(a)

