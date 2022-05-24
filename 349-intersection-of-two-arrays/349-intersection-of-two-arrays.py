class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        firstArray = set(nums1)
        secondArray = set(nums2)
        
        return firstArray & secondArray
        