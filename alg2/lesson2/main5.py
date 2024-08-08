'''

write

1如果这个文件本身存在，执行w操作的话，文件会被清空。
2 如果这个文件不存在，电脑会新建一个文件，并写



'''

a = ['1','2','3']
fp = open('C:\\Users\lmz\PycharmProjects\pythonProject/alg2\lesson2\cun','w',encoding='utf-8')    #单个\有可能出现错误

# for i in a:
#     fp.write(i+' ')

fp.writelines(a) #一股脑的全写入



fp.close()