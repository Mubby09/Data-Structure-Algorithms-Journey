# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        result = 0
        if root == None:
            return result

        if root.val >= low and root.val <=  high:
            result += root.val
            
        if root.val > low:
            result += self.rangeSumBST(root.left, low, high)

        if root.val < high:
            result += self.rangeSumBST(root.right, low, high)
            
        return result
            
                
        