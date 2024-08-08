'''

l1 = [1,2,4]

l2 = [3,7,2]

俩个列表本身是有序的

1合并到一起排序： sorted() 针对任意列表

2 i 0 j 0   双指针方式
result = [1,2,2,3,4,7]

def total_sort(l1,l2)
    result = []

    :return result
'''
def total_sort1(l1,l2):
    result = l1 + l2
    result = sorted(result)
    return result

def total_sort2(l1,l2):
    i = 0
    j = 0
    result = []
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1

    if i == len(l1):
        result = result + l2[j:]
    else:
        result = result + l1[i:]

        #
        # if max(l1) <= max(l2):
        #     result = result + l2
        #
        # else:
        #     result = result + l1
        return result


if __name__ == '__main__':
    a = [1,2,7]
    b = [2,3,4]
    c = total_sort2(a,b)
    print(c)




