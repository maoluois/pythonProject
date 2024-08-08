'''
递归

不断地调用自己（函数）

套娃

def f(n）:
    if n == 1:
        print(n)
    else:
        5*f(n-1)

f(5)
=5*f(4)
=5*4*f(3)
=5*4*3*f(2)
=5*4*3*2*1


简单的递归:每个数字都要做一件事的时候
或者说之后的状态和之前的状态有关





'''

def fib(n):
    n1 = 0
    n2 = 1
    if n<=1:
        return n

    temp = 0
    for i in range(n):
        temp = n1 + n2
        n1 = n2
        n2 = temp
    return temp

def fib2(n):
    if n<=1:
        return n
    else:
        return fib2(n-1) + fib(n-2)

'''
有初始条件即可用递归

'''