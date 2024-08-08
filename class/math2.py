'''

类   class  面向对象编程


'''

class Dog:
    # 变量
    # 函数
    name = 'cc'
    age = 1
    color = 'yellow'
    health = 100
    total_num = 0
    # 定量


    # inint 初始化函数
    def __init__(self,name,age,color):
        # 实例变量
        self.name = name
        self.age = age
        self.color = color
        Dog.total_num += 1  #辐射全局
    def speak(self):
        print('我的名字是：',self.name)

    def damage(self,hurt):
        print(self.health)
        self.health = self.health - hurt

        if self.health < 0:
            print('game over')
class Cat:
    def __init__(self,name,color,weigh):
        self.name = name
        self.color = color
        self.weigh = weigh

    def speak(self):
        print('我的名字是',self.name+'我的体重是',self.weigh)
        print('我的名字：{0}，我的体重：{1}'.format(self.name,self.weigh))
    def shout(self):
        print('喵喵喵')





if __name__ == '__main__':
    # 实例化
    dog1 = Dog('xx',5,'black')

    dog2 = Dog('vv',6,'red')
    print(dog1.speak())
    print(dog2.speak())

    cat1 = Cat('毛毛','橘黄色','15')
    print(cat1.speak())
    print(cat1.shout())
    dog1.damage(30)
    dog1.damage(30)
    dog1.damage(50)
    print(Dog.total_num)