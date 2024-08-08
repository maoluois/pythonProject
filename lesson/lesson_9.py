'''
1.求1-100质数函数的表达
2.复循环






'''

def prime(number1,number2):
    data_list = []
    for num in range(number1,number2+1):
        flag = 1
        for i in range(2,num):
            if num % i == 0:
                flag = 0
                break

        if flag == 1:
            data_list.append(num)

    return data_list




if __name__ == '__main__':

    # for num in range(2,101):
    #     flag = 1
    #     for i in range(2,num):
    #         if num % i == 0:
    #             flag = 0
    #             break
    #
    #     if flag == 1:
    #         print(num)
    data = prime(1,100)
    print(data)

    '''
    斐波那契数列：0，1，1，2，3，5，8....
    
    
    
    '''
    nterms = int(input('你需要几项'))
    n1 = 0
    n2 = 1
    count = 2
    if nterms == 1:
        print(n1)
    elif nterms == 2:
        print(n2)
    else:
        while count < nterms:
            num = n1 + n2
            n1 = n2
            n2 = num
            count += 1