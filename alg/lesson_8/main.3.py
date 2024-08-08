'''
高级的数据结构 class

节点:链表

数组【1，2，3，4，5，】
性质   可以用下标访问:计算机怎么存:连续的存在一起。

链表：
存储灵活，但是查找不变

'''
class Node:
    def __init__(self,x):
        self.x = x
        self.next = None
        

if __name__ == '__main__':
    a = Node(5)
    print(a.x)
    print(a.next)