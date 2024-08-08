# t 1870






def cal_hours(dist,mid):
    cost = 0
    for i in dist[:-1]:
        # 向上取整数且在整除为整数时为不向上取
        cost += (i + mid - 1) // mid  
    # 单独计算最后一次的耗时

    cost += dist[-1] / mid
    return cost



#[1,3,2], hour = 2.7

# [1,300]
# 找到最小的正整数，最后一个满足的
'''

mid = 150
left  =1 

1 +1 +2/150 < 2.7, 150 

1，150  -》75   1+1+2/75 
34  ok

27  ok

14 ok
[1,14]
[1,7]
[1,4] 1+1+2/4 <2.7
[1,2]->[2,4] mid =3  1+1+2/3  -》[2，3]   mid =2 不满足，[ ,3] 跳出训， 


'''


class Solution:
    def minSpeedOnTime(self, dist, hour):

        # 如果时间小于dist -1返回 -1
        if hour  <= len(dist) - 1:
            return -1
        
        # 设置二分查找边界
        left,right = 1, max(dict) * 100
        
        while left < right: # 跳出循环是最后一次，循环结束，是最后一次满足
            cost = 0
            mid = (left + right) // 2
            cost = cal_hours(dist,mid)
            if cost > hour:
                left = mid + 1 # 在最后left right相邻时，能使left = right
            else:
                right = mid
        return -1 if left == 10 ** 9 else left
