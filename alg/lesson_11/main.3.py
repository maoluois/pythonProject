

def check(list):
    a = sorted(list)

    l = len(a)
    n = 0
    m = 1
    flag = 0
    while m < l:
        if a[m] - a[n] == 1:
            flag += 1
            if flag == 5:
                return True

        n += 1
        m += 1

    return False

# in 和 not in


def find(L):
    for i in L:  # 只有使用权  如果用下标可以改变值
        temp = i
        flag = 0
        for j in range(4):
            temp += 1

            if temp in L:

                continue


            

            else:
                flag = 1
                break

        if flag == 0:
            return True

    return False