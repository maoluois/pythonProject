'''
单纯的并列关系，可以一个一个处理，从头到位，是一队


圆圈:
0，1,2,3,4,5
组成一个圈 从0开始删除第三个数，删除后的下一个数字开始计数，问删除2遍后剩下的序列
'''


def delete(i,numlist):
    # 第一次
    if i < len(numlist):
        numlist.remove(numlist[i - 1])

   # 第二次
    if len(numlist[i:]) >= i:
        numlist.remove(numlist[i + i - 2])
    else:
        temp = i - len(numlist[i:])
        numlist.remove(numlist[temp - 1])
