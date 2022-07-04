# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def sortArrToB(start_index, end_index):
            if start_index > end_index:
                return None
            
            mid = (start_index + end_index) // 2
            
            root = TreeNode(nums[mid])
            root.left = sortArrToB(start_index, mid - 1)
            root.right = sortArrToB(mid + 1, end_index)
            
            return root
        
        return sortArrToB(0, len(nums) - 1)
        