def find(num):
    num = str(num)
    a = 0
    flag = 0
    while a < 8:
        if flag == 0 and num[a] == '2':
            flag = 1
        if flag == 1 and num[a] == '0':
            flag = 2
        if flag == 2 and num[a] == '2':
            flag = 3
        if flag == 3 and num[a] == '3':
            return 1
        a += 1
    return 0

# if __name__ == '__main__':
#     count = 0
#     for i in range(12345678, 98765433):
#         i = str(i)
#         if '2' and '0' and '2' and '3' in i:
#             count += find(i)

#     print(98765432 - 12345678 + 1 - count)

import time
count = 0
start = time.time()
for i in range(12345678, 98765433):
    strnumber = str(i)
  # 依次包含 2,0,2,3 这个数字
    if "0" in strnumber and "3" in strnumber and strnumber.count("2") > 1 :
         # 依次包含 2,0,2,3 这个数字
        if find(i):
            count += 1
end = time.time()
print(end - start)
print(count)   