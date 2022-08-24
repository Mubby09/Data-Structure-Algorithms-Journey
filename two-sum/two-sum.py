class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashM = {}
        
        for index, num in enumerate(nums):
            difference = target - num
            if difference in hashM:
                return [hashM[difference], index]
            else:
                hashM[num] = index
        