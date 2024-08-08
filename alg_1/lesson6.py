# t 70 迭代



def f(n):
    if n == 1 or n == 0:
        return 1
    else:
        return f(n - 1) + f(n - 2)
    
# 实质是将数字全部拆开 递归

# 迭代
n = int(input())
a, b = 1, 1
for _ in range(n - 1): 
    # 从0到n - 1共n - 2 + 1项 b的下标是1 则刚好算到下标n
    a, b = b, a + b
print(b)







