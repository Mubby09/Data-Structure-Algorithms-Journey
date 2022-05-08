class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashT = {}
        
        for i, n in enumerate(nums):
            difference = target - n
            if difference in hashT:
                return [hashT[difference], i]
            
            hashT[n] = i
        