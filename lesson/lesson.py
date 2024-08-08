import random
if __name__ == '__main__':

    your_name = input('请输入你的名字:\n')
    print('欢迎来到猜数字游戏'+your_name)

    print('我猜了一个数字在1到100之间，你能猜到它吗？')

    random_num = random.randint(1,100)
    time = 0
    while time < 8:
        num = int(input('请输入你的数字:\n'))
        if num ==random_num:
            break
        elif num < random_num:
            print('你猜的数字小了。')
        else:
            print('你猜的数字大了。')

        time = time + 1

    if time < 8:
        print('恭喜你，你赢了^_^.')
    else:
        print('别灰心，再来一次你可以的^_^')


 

