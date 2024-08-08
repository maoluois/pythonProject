'''

num1 = [11,2,4,12]

num2 = [14,12,16,17]

交叉相减
'''


def Mx(numList1,numList2):
    p = 0

    for i in range(len(numList1)):
        for j in range(len(numList2)):

            result = abs(numList1[i] - numList2[j])

            if result > p:
                p = result
    return p
