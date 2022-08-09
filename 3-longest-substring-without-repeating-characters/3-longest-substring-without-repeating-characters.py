class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left_pointer = 0
        right_pointer = 0
        longest = 0
        
        while right_pointer < len(s):
            if s[right_pointer] not in charSet:
                charSet.add(s[right_pointer])
                right_pointer += 1
            else:
                charSet.remove(s[left_pointer])
                left_pointer += 1
            
            longest = max(longest, right_pointer - left_pointer)
        return longest
        