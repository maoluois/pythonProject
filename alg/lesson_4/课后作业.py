from 并序 import combine

def combine1(list1,list2,list3):
    list4 = []
    i = 0
    j = 0
    k = 0

    while i < len(list1) and j < len(list2) and k < len(list3):  # 出错分析 1，检验每个大部分 print()2.检验变量，判断出错的地方
        if list1[i] <= list2[j] and list1[i] <= list3[k]:
            list4.append(list1[i])
            i += 1
        elif list2[j] <= list1[i] and list2[j] <= list3[k]:
            list4.append(list2[j])
            j += 1
        elif list3[k] <= list1[i] and list3[k] <= list2[j]:
            list4.append(list3[k])
            k += 1

    if len(list1) == i:
        while k < len(list3) and j < len(list2):
            if list3[k] < list2[j]:
                list4.append(list3[k])
                k += 1
            else:
                list4.append(list2[j])
                j += 1
        if len(list2) == j:
            list4 += list3[k:]
        else:
            list4 += list2[j:]
        # list4 += combine(list3[k:],list2[j:])
    elif len(list2) == j:
        while k < len(list3) and i < len(list1):
            if list3[k] < list1[i]:
                list4.append(list3[k])
                k += 1
            else:
                list4.append(list1[i])
                i += 1
        if len(list1) == i:
            list4 += list3[k:]
        else:
            list4 += list1[i:]
        # list4 += combine(list3[k:],list1[i:])

    else:
        while i < len(list1) and j < len(list2):
            if list2[j] < list1[i]:
                list4.append(list2[j])
                j += 1
            else:
                list4.append(list1[i])
                i += 1
        if len(list2) == j:
            list4 += list3[k:]
        else:
            list4 += list2[j:]
        # list4 += combine(list2[j],list1[i])
    return list4

# 注意相等情况
if __name__ == '__main__':
    list1 = [6,8,15,17,21,24]
    list2 = [1,3,7,10,13,14]
    list3 = [4,5,8,9,12,19]

    a = combine1(list1,list2,list3)
    print(a)