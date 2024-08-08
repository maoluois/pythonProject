'''

1 认识了二叉树的数据结构
以及基本的队列的访问方式

递归的思想：递归算法

1 一般来说，自己调用自己 特征
2 需要有终止条件（没有的话，死循环）本质上是一种压栈（本质上申请内存）

f(4)

4*f(3)

4*3*f(2)

4*3*2*f(1)

4*3*2*1

:return 4 * (return 3*)



'''

def multiple(number):
    if number == 1:
        return 1
    else:
        return number*multiple(number-1)




a = multiple(6)
print(a)