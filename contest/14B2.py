
# 1
# case = [0 for _ in  range(4047)]
# for i in range(1, 2024):
#     for j in range(i + 1, 2024):
#         case[i + j] += i

# print(max(case))
# # 为什么相同面值硬币相加的情况不用考虑？ 只考虑奇数
# 2
sum = 0
for i in range(1, 1011):
    sum += i
sum = sum + 2023    # 2023以前不可能

for end in range(1012, 2023):
    new = 2 * end + 1    # 只考虑奇数
    start = new - 2023    
    sum2 = (end - start + 1) * (start + end) / 2
    if (sum2 > sum):
        sum = sum2

print(int(sum))        