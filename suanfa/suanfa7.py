'''
插入排序

[3,7,2,9,1,0,19,23]

[3]
[3,7]
[2,3,7]
[2,3,7,9]
[1,2,3,7,9]
......







'''

def insersort(list):
    for i in range(1,len(list)):
        value = list[i]
        j = i - 1
        while j >= 0:  #管移动的，是否需要移动
            if list[j] > value:
                list[j+1] = list[j]
            else:
                break

            j = j - 1
        list[j+1] = value
    return list






if __name__ == '__main__':
    num_list = [3,7,2,3,9,1,0,19,23]
    a= insersort(num_list)
    print(a)