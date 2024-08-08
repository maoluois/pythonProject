'''

1 类的所有变量的声明与调用

类变量
实例变量

类中：
self



类属性绑定：
原本没有这个变量。在变量外添加


'''


class Dog():
    # 类变量
    kind = 'taidi'

    def __init__(self,name):
        # 实例变量
        self.name = name
        self.age = 16
    def find(self):

        self.age += 1
        a = Dog.kind # 类变量要用 类名。变量名
if __name__ == '__main__':
    dog1 = Dog('jake')
    dog2 = Dog('rose')

    print(dog1.kind)
    print(dog2.kind)
    print(dog1.name)
    print(dog2.name)

    # 类实例属性绑定
    dog1.color = 'red'
    print(dog1.color)

    #类属性 (所有都有的)
    Dog.country = 'china'
    print(dog1.country)
    print(dog2.country)