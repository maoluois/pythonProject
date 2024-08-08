def findTarget(list):
    pass



def cR(head,foot):
    flag = 0
    ji = 0
    for ji in range(head + 1):

        if 2 * ji + 4 * (head - ji) == foot:
            flag = 1


    if flag == 1:
        return ji,head - ji
    else:
        return 0,0

def cJ(numberlist):
    l = sorted(numberlist)
    t = 1
    ji = 0
    if l[len(numberlist)-t] != l[len(numberlist)-t-1]:

        ji =  l[len(numberlist-t)] * l[len(numberlist-t-1)]


    return ji



# -1,-2代表倒数第一，二

def CJ1(numlist):
    a = 0

    for i in numlist:
        for j in numlist:
            if i != j:
                if i*j > 0:
                    a = i*j

    return a

def CJ2(numlist):
    n1 = max(numlist)

    numlist.remove(n1)

    n2 = max(numlist)

    return n1*n2






if __name__ == '__main__':
    a = [1,2,5,7,8]