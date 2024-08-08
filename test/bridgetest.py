
import math

def total(n):
    
    sum = 0
    for i in map(int, str(n)):
        sum += i
    return sum
        


cnt = 0
for l in range(100, 1000000):
    for r in range(2, int(math.sqrt(l))):
        if total(l % r) == 23 and l % r == 0:
            cnt += 1

print(cnt)