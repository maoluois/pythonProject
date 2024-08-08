'''

 # double = [[1, 2, 3, 9, 12], [2, 3, 5, 23], [7, 8, 56, 94, 5]]
如果说：发现数字在7-20之间的加起来求和，如果和大于25就终止返回和

'''

def he(doublelist,num):

    sum = 0
    for i in range(len(doublelist)):

        for j in range(len(doublelist[i])):
            if 7 <= doublelist[i][j] <= 20:
                sum += doublelist[i][j]
            if sum > num:
                return sum

    if  sum < num:
        return 0

def jisuan(doublelist):
    i = 0
    he = 0
    while i < len(doublelist):

        j = 0

        while j < len(doublelist[i]):
            if 7 <= doublelist[i][j] <= 20:
                he +=doublelist[i][j]

            if he > 25:
                return he
            j += 1
        i += 1

    if he < 25:
        return 0
if __name__ == '__main__':
    double = [[1, 2, 3, 9, 12], [2, 3, 5, 23], [7, 8, 56, 94, 5]]
    a = he(double,25)
    print(a)