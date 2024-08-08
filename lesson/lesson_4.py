if __name__ == '__main__':
    myName = 'luois 6#'
    # myName = input('你的名字是:\n')
    # x = 9
    # y = 8
    # print('欢迎你:',myName)
    # print('欢迎你:'+myName)
    # print('欢迎你%s,%s我们即将开始游戏%s:'%(myName,x,y))

  


    # Len = len(myName)
    # number = myName.count('i')  # 查找数量
    # print(Len,number)
    
    # temp = myName.split(' ')     # 分割成列表
    # print(temp[1])
    # print(temp)
   
    # index_1 = myName.index(' ')  # 索引在第个位置
    # print(index_1)




    # s = 'we are happy'
    # x = s.replace(' ','%')    # 替换
    # print(x)

    # a = myName.strip('#')  # 去除
    # print(a)

    j = len(myName)
    x = 'u'
    
    for i in range(j):
        if myName[i] == x:
            print('找到了%s'%x)    # 百分号后%s = %（一个变量）
            break
        else:
            print('查找失败')
            continue
    
    # for i in j:
    #     print(i)


