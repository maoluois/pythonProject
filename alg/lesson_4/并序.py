'''

合并思想：

俩个队列


[1,3,7,10,13,14]
[4,5,8,9,12,19]

列表合并要相加
'''
def combine(list1,list2):
    list3 = []



    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list3.append(list1[i])
            i = i + 1
        else:
            list3.append(list2[j])
            j = j + 1

    if i == len(list1):
        list3 += list2[j:]
    else:
        list3 += list1[i:]


    return list3
if __name__ == '__main__':

    f = [1,3,7,10,13,14]
    s = [4,5,8,9,12,19]

    # for i in range(len(s)):
    #     f.append(s[i])
    #     f.sort()
    # print(f)

    c = combine(f,s)
    print(c)
    