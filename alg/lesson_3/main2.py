def picture(data):
    x = []
    y = []

    for i in range(len(data)):
        x.append(data[i][0])
        y.append(data[i][1])
    print((min(x)-1,min(y)-1))

    print((max(x)+1,max(y)+1))



if __name__ == '__main__':


    data = []
    hang = int(input())
    for i in range(hang):
        temp = input().split(',')
        a = [int(i) for i in temp]
        data.append(a)
    # 获取输入进阶版
    picture(data)


