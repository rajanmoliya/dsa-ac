class Solution:
    def removeConsecutiveCharacter(self, s):
        res = "" # commment 
        
        for i in range(len(s)):
            if i == 0 or s[i] != s[i-1]:
                res += s[i]
        
        return res
