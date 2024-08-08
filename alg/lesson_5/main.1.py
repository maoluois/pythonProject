
'''


我从控制台输入 1，5，2，7，12，42
'''

def shift(s):

    temp = s
    result =[]
    for i in range(len(s)):
        temp = temp[1:] + temp[0]

        result.append(temp)

    return result

def shift2(s):
    i = len(s) - 1
    b = s
    while i - 1 > 0:
        b[i-1] = s[i]
    b[i] = s[0]

if __name__ == '__main__':
    # s = input()

    s = input()

