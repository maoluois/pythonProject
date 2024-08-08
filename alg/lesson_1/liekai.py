def lieKai(string,kw):

    b = len(string)
    if kw < b:
        # print(string[0:kw]) #可把0去掉
        # print(string[kw:b]) #若末尾无条件，b可删去
        print(string[:kw])
        print(string[kw:])
if __name__ == '__main__':
    lieKai('hello world', 4)

    a = [1,4,3,2]
    b = 'abcd'
    print(a[1:4])
    print(b[1:4])
    # print(a[4])
    # print(b[4]) #注意区分

