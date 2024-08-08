'''

1 检测错误

限定一些运行条件


自检查，报错

assert

断言，状态检查


'''


a = input()

assert type(a) == int # 如果要继续执行，a必须是整数

print(a)

# Example
def find(number):

    assert number >= 5
    a = number - 5
    return a

# print(find(1))

print(find(6))

a = input('请输入三个数')
a = a.split()
assert len(a) == 3