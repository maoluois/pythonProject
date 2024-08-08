# t 34






def searchleft(target, list):
    low = 0
    high = len(list) - 1
    
    while low < high - 1:        
        mid = ((low + high ) // 2) 

        if list[mid] >= target:
            high = mid
        else: 
            low = mid

    if list[low] == target:
        return low
    elif list[high] == target:
        return high
    else:
        return -1     

      
def searchright(target, list):
    low = 0
    high = len(list) - 1
    
    while low < high - 1:        
        mid = ((low + high ) // 2) 

        if list[mid] >= target:
            high = mid
        else: 
            low = mid

    if list[high] == target - 1:
        return high
    elif list[low] == target - 1:
        return low
    else:
        return -1
    
    
if __name__ == '__main__':
    target = int(input("请输入你要查找位置的数\n"))
    result = []
    nums = [5, 7, 7, 8, 8, 10]
    
    if nums == []:
        print([-1, -1])

    left = searchleft(target, nums)
    result.append(left)
    right = searchright(target + 1, nums)
    result.append(right)
    print(result)