'''
1. 常见的算法练习
2. 常见的数据结构: （str ,data:int,float,list,dic,set
    高级版: 包含链表，数组，栈和队列，树，图，数据结构

算法 : 指针的想法，时间和空间复杂度的计算，递归算法（懂得原理），DFS（深度搜索），BFS（广度搜索），图相关
last : 5大排序算法，和搜索算法

'''


'''
俩个有序的列表
[1,2,4]
[3,4,7,8,12]

合并成一个
[1,2,3,4,4,7,8,12]
'''

def metrgeList(list1,list2):

    p = list1 + list2

    p = sorted(p)
    return p

def metrgeList1(list1,list2): #用空间换时间
    p = 0
    t = 0
    list3 = []

    while len(list1) > p and len(list2) > t:

        if list1[p] <= list2[t]:
            list3.append(list1[p])

            p += 1

        else:
            list3.append(list2[t])
            t += 1



    if t == len(list2):
        list3 += list1[p:]
    elif p == len(list1):
        list3 += list2[t:]

    return list3







if __name__ == '__main__':
    list1 = [1,2,3]
    list2 = [1,2,3]
    print(metrgeList1(list1,list2))

