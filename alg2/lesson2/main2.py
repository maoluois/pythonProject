'''

读写文件


'''

class Node():

    def __init__(self,data=None,next=None):

        self.data = data
        self.next =  next



a = Node(2)
b = Node(3)

a.next = b

print(a.data)
print(b.data)