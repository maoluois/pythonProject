def kMax(num_list,k):
    num_list.sort()
    return num_list[-k:]

def moveSame(num_list):
    num = set()
    for i in num_list:
        num.add(i)
    return num









if __name__ == '__main__':
    '''
    列表
    数字
    字符串
    字典
    集合
    
    去除重复的数
    1,2,2,4,4,5,7,7,8
    用双指针法进行多次比较
    1，2先比
    没有相同的就两个都向后推
    2，2比较有相同就删去一个
    以此类推
    
    i = 0
    j = i+1 
    while j < len(len_list):
        if num_list[i] == num_list[j]:
            num_list.remove(num_list)
    
    
    
    
    '''

    # dict_1 = {}
    # dict_1['mingZhi'] = 180
    # dict_1['xiaoKang'] = 183
    # print(dict_1)
    #
    # a = [1,2,3,4]
    # jihe = set()
    #
    # for i in a:
    #      jihe.add(i)
    # print(jihe)


    # exam = [1,2,3,3,4,67,89,56,0,98]
    # b = kMax(exam,5)
    # print(b)
    # exam.sort()
    # print(exam)
    #
    #
    # for i in range(len(exam)):
    #     if i > 4:
    #         print(exam[i])
    # print(exam[5:])
    # print(exam[-5:])

    #
    # a = set(exam)
    # print(exam)
    #
    #
    # n = moveSame(exam)
    # print(n)

    zfc = input('请随意输入一串字符\n')
    print(set(zfc))



















































