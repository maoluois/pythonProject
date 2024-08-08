'''

高级数据结构入门：

数组   【】

块数据
class




'''


class Dog:
    def __init__(self,name,age):

        self.name = name
        self.age = age

class Node:
    def __init__(self,data=None,next=None): #默认值
        self.data = data
        self.next = next


def visit(node:Node):
    # 我们一般把第一个节点当做头结点，不轻易移动

    p = node
    t = 0
    while p:  # 当node为None时停止

        p = p.next

        t += 1

    return t

'''

求出链表的最大值，并告诉链表上有几个
'''

def findMax(node:Node) -> list:
    p = node

    count = 0
    max = p.data

    while p:
        count += 1
        if p.data > max:
            max = p.data
        p = p.next

    return [max,count]

def Ji(node:Node):
    p = node

    ji = 1

    while p:
        ji = ji * p.data

        p = p.next
    
if __name__ == '__main__':
    # dog1 = Dog('小黑',8)
    #
    # print(dog1.name)
    # print(dog1.age)

    a = Node(1)
    b = Node(2)
    c = Node(10)
    a.next = b
    b.next = c

    #单纯的一个类名代表的是地址
    # print(a)
    # print(b)
    #
    # a.next = b
    #
    # print(a.next.data)

