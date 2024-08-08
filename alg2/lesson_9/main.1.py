'''

def DFS(node):
    if node == None:
        :return
    print(node.data)

    DFS(node.leftchild)
    DFS(node.rightchild)

'''

# 先序访问，把操作放在前

def DFS_pre(node):
    if node == None:
        return
    print(node.data)
    DFS_pre(node.leftchild)
    DFS_pre(node.rightchild)

def DFS_mid(node):

    if node == None:
        return


    DFS_pre(node.leftchild)
    print(node.data)

    DFS_pre(node.rightchild)


def DFS_af(node):
    if node == None:
        return

    DFS_pre(node.leftchild)
    DFS_pre(node.rightchild)
    print(node.data)

