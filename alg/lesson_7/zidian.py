'''
字典： dict = {'{':'}','[':']','(':')'}

3x - 2y = 3
x - 2y = 5
'''
import sympy

a = [1,3,5,7,9]
a.insert(1,2)
print(a)

dic = {'{':'}','[':']','(':')'}
del dic['{'] #用函数删除
print(dic)