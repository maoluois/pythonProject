'''
一个数据结构的完整格式。

1 初始化方式（生成）
2 大多数常用的方法（赋值，增删改查）


list():列表
linklist():链表



'''


class Node():

    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Link_list():
    def __init__(self): # 只有第一次才会调用
        self.head = None  # 第一个节点，第一个叫作头

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def append(self,item):
        '''向尾部添加元素'''
        node = Node(item)
        if self.is_empty():
            self.head = node # self指全局变量，即一变整个类中的都变
        else:
            # 如果不是空的，走到最后，在最后一个位置添加。
            a = self.head
            while a.next is not None:
                a = a.next
            a.next = node

    def visit(self):
        #访问所有元素
        a = self.head
        while a is not None:
            print(a.data)
            a = a.next

    def length(self):
        a = self.head
        count = 0
        while a is not None:
            a = a.next
            count += 1
        return count

    def find(self,item):
        a = self.head
        flag = 0
        while a is not None:
            if a.data == item:
                flag = 1
            a = a.next

        if flag == 1:
            return True
        else:
            return False
if __name__ == '__main__':

    L = Link_list()
    for i in range(10):
        L.append(i)

    print(L)
    L.visit()
    print(L.length())
    print(L.find(5))
    print(L.find(15))