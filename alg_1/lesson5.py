# 字串
"""
bcdef

字串: b bc bcd
子序列: bde
t 1044
"""

# 超时间了 要缩减需要动态规划
# 思路：大滑动框滑动寻找 （哈希表）
def Find(s):
  
    if len(set(s)) == len(s):
        return ""

    for i in range(len(s)):
        j = len(s) - i
        record = []
        for count in range(i + 1):
            cut = s[count : count + j]
            record.append(cut)
            if len(set(record)) != len(record):
                return cut

if __name__ == "__main__":
    s = input()
    a = Find(s)
    print(a)

          
            
           
            



