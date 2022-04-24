#from collections import Counter 
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        odd_count = 0
        for k, v in d.items():
            if v % 2 != 0 and odd_count == 0:
                odd_count +=1
            elif v % 2 != 0 and odd_count != range(0, 2):
                return False
        return True