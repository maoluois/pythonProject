'''
class node:
    def __init__(data):
        self.data = data
        self.next = None


已有链表倒数的第k个

def finK(k,linkList）

    :return  (k)node.data



'''




def fink1(k,linkList): # 普通思想
    count = 0
    p = linkList
    while p:
        count += 1
        p = p.next

    num = count - k + 1

    p = linkList
    count2 = 0
    while p:
        count2 += 1
        if count2 == num:
            print(p.data)
            break

        p = p.next


def fink2(k,linkList):  # 高级思想

    # 相差k - 1个

    after = linkList
    before = linkList

    num = k - 1
    while num:  # num = 0 结束
        after = after.next
        num -= 1

    while after.next:
        after = after.next
        before = before.next

    return before.data



