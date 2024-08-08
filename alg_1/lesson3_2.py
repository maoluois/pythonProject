# 哈希表自创做法


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        j = 0
        res = 0
        
        if len(s) == 0:
            return len(s)

        for i in range(len(s)):
            hash = s[j: i]
           
            if s[i] in hash:
                res = max(res,i - j)
                for j in range(j, i):
                    if s[j] == s[i]:
                        j += 1
                        break
            res = max(res,i - j + 1)
            
        
        if len(hash) - 1 > res:
            res = len(hash) - 1

        return res
    
