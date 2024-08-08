'''
树 tree


'''
# 子结构

class Node:
    def __init__(self,data):
        self.data = data

        self.leftchild = None
        self.rightchild = None

# 树 基础的结构

class Tree:
    def __init__(self):
        self.root = Node('root')

    def add(self,item):

        node = Node(item)
        if self.root == None:
            self.root = node
        else:
            lie = [self.root]
            while len(lie):
                p = lie[-1]  # 最后一个

                if p.leftchild != None:
                    lie.append(p.leftchild)
                else:
                    p.leftchild = node  # 最后一个左孩子必定为空
                    break

                if p.rightchild != None:
                    lie.append(p.rightchild)

    def visit(self):
        lie = []
        # 出 print
        if self.root != None:


            lie.append(self.root)

            while len(lie) > 0:
                p = lie[0]
                if p.leftchild != None:
                    lie.append(p.leftchild)
                elif p.rightchild != None:
                    lie.append(p.rightchild)

                print(lie.pop(0).data)




if __name__ == '__main__':
    tree1 = Tree()
    for i in range(5):
        tree1.add(i)

    tree1.visit()
    # a = Node(1)
    # b = Node(2)
    # c = Node(3)
    # a.leftchild = b
    # a.rightchild = c


    # print(a.data)
    # print(a.rightchild.data)
    # print(a.leftchild.data)

    # lie = []
    # lie.append(1)
    # lie.append(2)
    # lie.append(3)
    # a = lie.pop(0) # pop 出队 ，int 出第几个
    #
    # print(a)
    # print(lie.pop(0))