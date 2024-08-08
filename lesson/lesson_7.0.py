'''



函数


'''

def qiuhe(num1,num2):
    sum = 0

    for i in range(num1,num2+1):
        sum = sum + i
    return sum

def jiOu(num):
    if num % 2 == 0:
        return 1
    else:
        return 0





if __name__ == '__main__':


    # b = qiuhe(1,100)
    # print(b)

    m = jiOu(8)
    if m:
        print('偶数')