'''

self

1,

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

    def remove(self,number):

        p = self.head
        q = None # q代表p的前一个

        while p is not None:
            if p.data == number:
                # 三步走：首中尾
                if q is None:
                    self.head = p.next
                else:
                    q.next = p.next #正常的做法
                return True
            else:
                q = p
                p = p.next

    def insert(self,index,number):#一定要检查bug

        if index < self.length():
            new_node = Node(number)
            p = self.head

            for i in range(index-1): #index是下标
                p = p.next

            new_node.next = p.next #先接后面
            p.next = new_node

        else:
            self.append(number)





if __name__ == '__main__':
    L = Link_list()
    for i in range(10):

        L.append(i)


    L.visit()
    print(' ')
    L.remove(5)
    L.visit()
    print(' ')
    L.insert(2,100)
    L.visit()
    print(' ')
    L.insert(15,20)
    L.visit()
