pass
'''

最值：
最大值，最小值。
[1,4,5,-1,-9,8]
求最大和的连续子序列


[-2,1,-3,4,-1,2,1,-5,4]
'''

# 基础版
# 求所有的和，找最大值
'''
思路扩展：总体的思想

总和的范围
一堆数字。一个一个加（后面的数字是不知道的）
当我的和大于0，只有后面还有正就会一直增大。
当和小于0.就应该舍弃，从当前的下一个开始
当前如果加上一个数和小于0的。加上后面的数，都让后面的数字更小了
把前面看成整体

找开头好法
但是结尾要特殊处理（始终有个数保存最大值也行，舍弃max

'''

def find(list):
    p = []
    sum = 0

    for i in range(len(list)):
        # 让每个数得到开头的机会
        sum = list[i]
        if sum > 0:
            for j in range(i+1,len(list)):
                sum += list[j]
                p.append(sum)

    return max(p)

def find2(list):
    max_he = 0
    he = 0
    for i in range(len(list)):

        if he < 0:
            he = list[i]
        else:
            he += list[i]
            if he > max_he:
                max_he = he

    return max_he
    
if __name__ == '__main__':
    a = [1,4,5,-1,-9,8]
    print(find(a))

