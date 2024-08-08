

#
#
# def dfs(n, ):
#     global x
#     if x == n - 1:
#         x += 1
#         return
#
#     a[n - 1] = 0
#     a.append()



if __name__ == '__main__':
    T = int(input())
    while T > 0:
        n = int(input())
        x = 0
        a = [0] * int(1e5 + 10)
        a[0] = 0
        a[1] = 0
        for i in range(0, n):
            if i + 1 == n - 1:
                i = -1
            if i + 1 > n - 1:
                i = -2
            if a[i] == 0 and a[i + 1] == 1:
                a[i + 2] = 0
            elif a[i] == 0 and a[i] == 0:
                a[i] = 0
            elif a[i + 1] == 1 and a[i + 2] == 1:
                a[i + 3] = 0
            else:



        T -= 1