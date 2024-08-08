
def runnian(year):

    if year % 400 == 0:
        return 1
    elif year % 4 == 0 and year % 100 != 0:
        return 1
    else:
        return 0





def qiuhe(num_list):


    sum = 0
    for i in range(len(num_list)):
        sum = sum + num_list[i]

    return sum

#二分查找
def er_fen(num_list,key):
    left = 0
    right = len(num_list) - 1
    while left <= right:
        mid = (left+right) // 2  #二分
        if key > num_list[mid]:
            left = mid + 1
        elif key < num_list[mid]:
            right = mid - 1
        else:
            return mid + 1
    return -1

def double_num(numberlist):
    for i in range(len(numberlist)):
        for k in range(len(numberlist[i])):
            print(numberlist[i][k])

    for item in numberlist:
        for j in item:
            print(j)


if __name__ == '__main__':
    a = [1,4,3,2,7]
    # b = qiuhe(a)
    # print(b)

    l = 1984
    n = runnian(l)
    print(n)

    c = er_fen(a,7)
    print(c)

    double = [[1,2,3],[2,3,5,1],[7,8,94,5]]
    k = double_num(double)
    print(k)