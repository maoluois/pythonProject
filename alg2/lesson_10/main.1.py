'''
动态规划：

题目：
给定一个 整数数组nums，找到一个具有最大和的连续字数组（子数组最少包含一个元素），返回其最大和

nums = [-2,1,-3,4,-1,2,1,-5,4]

(1)动态规划：

递归：向下，深处。从后往前推

动态：横向发展，一步一步出结果，上一步和前一步有关，找关系，找表达式，递推方程

数学问题：

nums:List有n个长度
下标：0 - （n-1）

f(i):代表以i结尾的连续子数组和的最大值

求的答案： max{f(i)}    0 <= i <= n-1

    f(i) = num[i] + f(i-1)
    or
    f(i) = num[i]


(2)
    找关系完成!!
    f(i) = max{f(i) = num[i] + f(i-1),f(i) = num[i]}

(3)编程：
'''
def findList(num:list)-> int:
    max_answer = num[0]

    pre_he = 0

    for i in range(len(num)):
        if pre_he < 0:
            pre_he = num[i]
        else:
            pre_he += num[i]

        if pre_he > max_answer:
            max_answer = pre_he

    return max_answer