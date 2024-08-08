# def getSameChar(string):
# 函数1：获取字符串中连续相同的字符
# assd -> [s]
# 1,把所有字符串输出
# 2,访问的时候看下一个是否相同，如果相同，就保存






# 函数2：字符串中相同的字符
# asdsgbccomo


# 函数3：判断一个字符串 是不是另一个字符串的子序列（可以不连续）

# asd , aghskd 是的

def get_same_char(input_str):
    # 访问方式可以和列表一样
    # 第一种，可以i直接获取元素，没法获取位置，下标
    # for i in inpit_str
    #     print(i)
    #     pass
    result = []
    for i in range(len(input_str)-1):


    # i代表第几个
        if input_str[i] == input_str[i + 1]:
            result.append(input_str[i])
    return result


def get_repeat_char(input_str: str) -> list:
    result = []
    for i in range(len(input_str)-1):

        if input_str[i] in result:
            continue

        for j in range(i+1,len(input_str)):

            if input_str[i] == input_str[j]:

                result.append(input_str[i])
                break
    return result


def judge_subsequence1(sequence,input_str):
    result = []
    sub_result = []

    for i in range(len(sequence)):

        if sequence[i] in result:
            continue

        if sequence[i] in input_str:
            result.append(sequence[i])

    for j in range(len(input_str)):
        sub_result.append(input_str[j])


    if sub_result == result:   #??为啥有黄线

        return 'yes'

    else:
        return 'no'


# 不换成列表，用字符串可不可以？
# break 和 countinue 的用法差别及具体内涵？
# askksa ksa 的case无法完成



def judge_subsequence2(sequence,input_sequence):

    # result = []
    # sub_result = []

    # for k in range(len(input_sequence)):
    #     sub_result.append(sequence[k])
    pos = 0
    for i in range(len(input_sequence)):
        # sub_result.append(input_sequence[i])
        flag = 0
        for j in range(pos,len(sequence)):

            if input_sequence[i] == sequence[j]:
                # result.append(sequence[j])
                pos = j
                flag = 1
                break

        if flag == 0:
            return 'no'

    return 'yes'

if __name__ == '__main__':
    a = 'asd'
    b = 'aasssssddddd'
    c = judge_subsequence2(a,b)
    print(c)