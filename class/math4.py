'''
模糊查找


 a*  以a开头的   apple about
a*e  apple   a*e
*a   以a结尾  a，


正则表达式:匹配你需要的字符串，你就需要一个特定的命令，组成命令的表达式
^匹配字符串的开头
$匹配结尾的符号
.匹配任意字符串（除了换行符）
* 表示0或者多个
'''


import re
import time


if __name__ == '__main__':
    result = time.time()
    local_time = time.localtime(result)
    temp = time.asctime(local_time) #自带格式化
    print(local_time)
    print(result)
    print(temp)
    # 时间戳
    # line = 'cats are smater than dogs'
    # temp = r'^a.*e$'
    # result = re.findall(r'.[temp]',line)
    # print(result)
    # formate
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) #  可有参数，有的话就翻译，自己格式化
    time.sleep(10)  #多少秒，强制执行等待，就如广告一样
    print('已经过了一段时间')




