
def GYS(num,M,N):
    n = 1
    p = []
    while n <= num:

        if num % n == 0 and num//n <= M and n <= N:
            p.append((num//n,n))
        n += 1
    return p

def findL(point,M,N,result):

   value = point
   re_list = GYS(value,M,N)


   for i in re_list:
       if i not in result:
           if i[0] == M and i[1] == N:
               return 'yes'
           else:
               findL(point,M,N,result)
               result.append(point[i[0][i[1]]])


if __name__ == '__main__':
    a = 6
    print(GYS(6,3,2))