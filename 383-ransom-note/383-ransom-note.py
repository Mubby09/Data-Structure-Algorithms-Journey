class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # charCountInR = Counter(ransomNote)
        charCountInR = {}
        
        for i in ransomNote:
            if i in charCountInR:
                charCountInR[i] += 1
            else:
                charCountInR[i] = 1
                
        
        for c in magazine:
            if c in charCountInR:
                charCountInR[c]-= 1
                if charCountInR[c] == 0:
                    del charCountInR[c]
            
                    if charCountInR == []:
                        return True
        return not charCountInR