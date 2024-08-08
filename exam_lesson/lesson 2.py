def is_sequence(sequence,input_sequence):

    i,j = 0,0
    while i < len(sequence) and j <len(input_sequence):
        if sequence[i] == input_sequence[j]:
            i += 1
        j += 1

    if i == len(sequence):
        return True
    else:
        return False

    # return i == len(sequence)
    # 双指针思想



    # 合并俩个列表
def merge_sorted_lists(lst1,lst2):
    i,j = 0,0
    result = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            i += 1

        else:
            result.append(lst2[j])
            j += 1

    result += lst1[i:]
    result += lst2[j:]
    return result


    # 求列表第k大的元素
import random
def quick_select(nums,k):  # 有问题的

    pivot = random.choice(nums)
    left = [x for x in nums if x <= pivot]
    right = [x for x in nums if x >= pivot]
    if k <= len(right):
        return quick_select(right,k)

    elif k > len(nums) - len(left): # 第k大的在左边，减去右边的个数 比如右边有一个，下次第k-1大的就可以
        return quick_select(left,k - (len(nums) - len(left)))

        # 都不在上面俩个里面，就只剩当前随机选择的pivot，直接返回
    else:
        return pivot

def quick_select2(nums, k):
    while True:
        pivot = random.choice(nums)
        left, mid, right = [], [], []
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                mid.append(num)
            else:
                right.append(num)
        if k <= len(right):
            nums = right
        elif k > len(right) + len(mid):
            k -= len(right) + len(mid)
            nums = left
        else:
            return mid[0]
# 二分法
if __name__ == '__main__':
    # if is_sequence('asd','assf'):
    #     print('yes')
    # else:
    #     print('no')

    # list1 = [1,4,5,7,8]
    # list2 = [2,3,6,7,8,9]
    # a = merge_sorted_lists(list1,list2)
    # print(a)
    nums = [1,2,33,6,77,8,899]

    b = quick_select2(nums,4)
    print(b)