def decode(list):
    flag = 0
    for i in range(len(list)):
        list[i] = 9 - list[i]
       
    
    
    flag = list[1]
    list[1] = list[2]
    list[2] = flag

    flag = list[0]
    list[0] = list[3]
    list[3] = flag


if __name__ == '__main__':
   
   
    num = int(input("请输入你要解密的数字\n"))
    list1 = [num // 1000, num % 1000 // 100, num % 100 // 10, num % 10]
   
    decode(list1)
    
    if list1[0] == 0:
        print("这不是四位数噢")
    else:
        thous = list1[0] * 1000
        hund = list1[1] * 100
        ten = list1[2] * 10
        print(thous + hund + ten + list1[3])

   