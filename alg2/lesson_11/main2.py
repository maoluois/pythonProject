'''
简单图。

A到D有没有路

有 返回 ture，没有就返回False

A:[b,c]

1.B-->D 或者C-->D有没有路

B:[A，C，D] 成功

C:[]




2、图当中有没有环（绕一圈）：

A->A 有没有路
B->B
C->c
D->D

查找路径的一个函数 从任意点m,到任意一点n的路径。
'''

graph = {
    1:[1,2],
    2:[2,3,4],
    3:[1,2,4],
    4:[1,2]

}

# A到D

# graph[graph['A'][0]]
flag = [0]*len(graph)  # 矩阵*任意一个数都可以生成矩阵
print(flag)


def path(m,n,flag):

    if flag[m] == 1:
        return False

    next_path = graph[m]

    flag[m] = 1 # 代表已经访问过
    if m == n:
        return True

    lu = False

    for i in next_path:

        lu = path(i,n,flag)
        if lu == True:
            return lu


    return lu

