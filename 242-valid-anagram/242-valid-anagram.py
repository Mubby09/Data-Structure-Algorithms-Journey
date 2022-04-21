class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Check if length of s and t are equal
        if len(s) != len(t):
            return False
        #Initialize both hash tables
        countS, countT = {}, {}
        for i in range(len(s)):
            #Build key value pairs for each character in the hash tables
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        for c in countS:
            #Check if values of each characters in both hash tables are equal
            if countS[c] != countT.get(c, 0):
                return False
        return True