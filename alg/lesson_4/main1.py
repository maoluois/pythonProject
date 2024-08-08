'''

输入一个数，输出逆序数字

[a:b:c]从a到b（不包含【b】），间隔c个，后面减去前面的次序得到的数字
[:b]不填代表所有
[b:]b到最后一个  []代表列表
'''

def reverse(number):
    number_str = str(number)
    print(number_str[len(number_str)::-1])


def reverse2(number):

    temp = number
    a = 0
    while temp > 0:
        wei = temp % 10

        a = a*10 + wei # 你后面有多少位就要乘多少个10，小数点一直一直在往右走+wei

        temp = temp // 10

        return a










a = int(input())
reverse(a)

numlist = [3,21,5,23,6,31]

print(numlist[::2])   # 奇数位
print(numlist[1::2])    # 偶数位
print(numlist[::-1])    # 倒序









