'''

[1,2,5,4,1]


怎么快速找重复的元素

1 先想最简单的方式：循环就可以

[1,1,2,4,5]
相等的在一起

'''

def findRepeat(numlist):  #
    result = []

    for i in range(len(numlist)):
        for j in range(i+1,len(numlist)):
            if numlist[i] == numlist[j]:
                result.append(numlist[i])

    return result


def findReapt2(numList):
    result = []
    l = sorted(numList)
    s = len(numList)
    t = 0
    while t <= s - 2:
        if l[t] == l[t+1]:
            result.append(l[t])
        t += 1

    return result

def findRepeat3(numList):
    result = []
    a = set()

    for i in numList:
        if i in a:
            result.append(i)
        else:
            a.add(i)

    return result

# 自动排序 用列表不会

if __name__ == '__main__':
    a = [1,2,5,4,1]
    print(findRepeat3(a))







