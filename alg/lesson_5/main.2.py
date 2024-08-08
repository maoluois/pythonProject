'''

[1,12,16,3,8,10,7]

求组成的长方形的最大面积
'''



def S(list):
    p = []
    for i in range(len(list)):
        for k in range(i+1,len(list)):
            y = min(list[i],list[k])
            x = k - i
            s = x * y
            # print(s)
            p.append(s)

    return max(p)


def S2(list):
    i = 0
    j = len(list) - 1
    p = []
    while i < j:

        s = (j-i) * min(list[i],[j])
        p.append(s)
        temp = min(list) - 1
        if list[i] <= list[j]:
            while list[i] <= temp:
                i += 1
        #加到比我的temp大
        if list[j] <= list[i]:
            while list[j] <= temp:
                j -= 1

    return max(p)




if __name__ == '__main__':

    a = [1, 12, 16, 3, 8, 10, 7]
    k = S(a)
    print(k)

