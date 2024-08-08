'''

a = [1,4,7,12,16]

是一个递增序列

给定一个number
1 如果在a里面，返回这个数字的下标

2 不在里面，找到插入后仍为递增序列的位置，返回下标



'''
def particular_find(list,number):

    if number in list:
    #     t = 0
    #     while t < len(list):
    #         if list[t] == number:
    #             return t
    #
    #         t += 1

        return list.index(number)


    else:
        # if number > max(list):
        #     return len(list) - 1

        for i in range(len(list)):
            if number < list[i]:
                return i

        return len(list)



