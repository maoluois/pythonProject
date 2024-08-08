'''

如果一个n位正整数等于其各位数字的n次方之和，则称该数为阿姆斯特朗数。
例如


'''
def amstls(min,max):
    result = [] #有效范围


    for num in range(min,max+1):
        n = len(str(num))
        temp_res = 0
        res = num
        while res > 0:
            zui_hou = res % 10
            res = res // 10  # 舍掉最后一位

            temp_res += zui_hou ** n


        if temp_res == num:
            result.append(temp_res)
    return result

if __name__ == '__main__':


    x = amstls(1,100)
    print(x)
