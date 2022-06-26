# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def are_trees_valid(root, low_range = float('-inf'), high_range= float('inf')):
        
            if not root:
                return True
            elif not low_range < root.val < high_range:
                return False
            return (are_trees_valid(root.left, low_range, root.val) and are_trees_valid(root.right, root.val, high_range))
        
        return are_trees_valid(root)
        
        
        