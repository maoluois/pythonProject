


class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


'''

查找链表中小于10的数字

'''
def findNumber(node:Node):
    p = node
    n = []
    while p:

        if p.data < 10:
           print(p.data)

        p = p.next


def delete(node:Node):

    p = node
    count = 0
    while p:
        count += 1
        if p.data > 10:
            break
        p = p.next

    number = 0
    q = node
    while q:
        number += 1
        if number == count - 1:
            q.next = q.next.next
            break

        q = q.next
    m = node
    while m:
        print(m.data)
        m = m.next

def delete2(node:Node):
    q = node
    p = node.next

    while p:
        if p.data > 10:
            q.next = p.next
            break
        q = q.next
        p = p.next

    m = node
    while m:
        print(m.data)
        m = m.next
def insert(k,number,node:Node):
    p = Node(number)
    q = node
    number = 0
    while q:
        number += 1
        if k - 1 == number:
            p.next = q.next
            q.next = p
            break
        q = q.next
    m = node
    while m:
        print(m.data)
        m = m.next



if __name__ == '__main__':
    a = Node(3)
    b = Node(7)
    c = Node(12)
    d = Node(18)

    a.next = b
    b.next = c
    c.next = d

    # findNumber(a)
    insert(3,10,a)