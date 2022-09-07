class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumOfAllNumbers = sum(nums)
        
        lengthOfArray = len(nums)
        
        actualSum = (lengthOfArray * (lengthOfArray + 1)) // 2
        
        return actualSum - sumOfAllNumbers
        