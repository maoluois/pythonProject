#-*-coding:utf-8-*-
'''


读写文段
1 读三种
#

readlines():返回的是包含所有行数的【列表】  可以进行处理  整理成一行
readline():读取的只有一行
read():直接读取所有数据

write
# '''

#
fp = open('C:\\Users\lmz\PycharmProjects\pythonProject/alg2\lesson2\chinese','r',encoding='utf-8')    #单个\有可能出现错误
a = fp.readlines()

for line in a:
    line = line.strip('\n')
    if len(line) != 0:
        print(line)

fp.close()