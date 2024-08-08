#-*-coding:utf-8-*-
'''
萧炎出现在哪一行，第几个单词
'''
if __name__ == '__main__':

    fp = open('C:/Users\lmz\PycharmProjects\pythonProject\data.txt','r',encoding='utf-8')#编码中文化
    count = 0
    hangshu = 0
    result = []
    for line in fp.readlines():

        line = line.strip('\n')
        line = line.lstrip('\t') #去掉制表符
        line = line.lstrip()  # 去头去尾，整理格式，去掉空格(默认是空格）

        if len(line) != 0:
            hangshu += 1


            print(line)
        #     print(type(line))
        # print(line.count('萧'))

            temp = line.count('萧炎')
            if temp > 0:

                weizhi = line.index('萧炎')
                hang = [hangshu,weizhi]
                result.append(hang)
            count += temp

    print(result)


    print(count)

    fp.close()


