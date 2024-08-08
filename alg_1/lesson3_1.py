# t3





s = input()
flag = 0
temp_len = len(s)
while temp_len > 0:
    # 找出当前长度的所有子串
    for i in range(len(s)- temp_len + 1):
        # print(a[i: temp_len + i])
        # # 判断是否有重复的，找到第一个没有重复的，就是最长的

        if len(s[i: temp_len + i]) == len(set(s[i: temp_len + i])):
            print(s[i: temp_len + i])
            print(len(s[i: temp_len + i]))
            flag = 1
            break
   
   
    if flag == 1:
        break
    
    temp_len -= 1
