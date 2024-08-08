def cost(spd):
    pass



def check(time, hour):
    if time < hour:
        return 1
    else:
        return 0

def minSpeedOnTime(dist, hour):
    if hour < 2:
        return -1
    right = dist[2] / 0.01
    left = 0
     
    while right > left:
        spd = (right + left) // 2
        time = cost()
        if check(time, hour):
            right = spd
        else:
            break
    return int(spd)            
      
    



if __name__ == '__main__':
    a = list(map(int ,str(input("dist = ")).split(",")))
    b = float(input("hour = "))
    
    c = minSpeedOnTime(a, b)
    print(c)