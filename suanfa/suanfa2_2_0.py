'''

1 变量的范围
  h = [1,2,45,79,8,7]
  计算列表中有没有俩个数的和为9
  每个函数值都用作用范围
'''


def jisuan(a):  # b叫形式参数，只获取值
    # 局部变量不改变全局变量

    a = a + 3


    return a

def jisuan2():
    global a    #全球的 代表全局变量 改变作用域
    a = a + 3
    return a

if __name__ == '__main__':
    a = 5 #实际参数。他表示事实纯在的
    c = 6


    C = jisuan(c)
    print(C)




