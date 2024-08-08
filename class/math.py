'''
1.函数的跳文件运用
2.质数的求和算法（and的使用）




'''






from lesson_9 import prime


if __name__ == '__main__':
    a = prime(1,100)
    print(a)
    for num in (a):
        for he in (a):
            if he + num == 100 and num <= he:
                print(num,he)