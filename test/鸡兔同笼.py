'''
输入

笼子中 头 的数量
笼子中 脚 的数量
输出

笼子中 鸡 的数量
笼子中 兔子 的数量
'''

def JiTu(numhead,numfeet):
    Jnum = 0
    Rnum = numhead
    while Jnum + Rnum == numhead and numfeet != Jnum * 2 + Rnum * 4:

        Jnum += 1
        Rnum -= 1

    return Jnum,Rnum

if __name__ == '__main__':
    numhead = int(input('请输入头的数量'))
    numfeet = int(input('请输入脚的数量'))

    a = JiTu(numhead,numfeet)
    print(a)