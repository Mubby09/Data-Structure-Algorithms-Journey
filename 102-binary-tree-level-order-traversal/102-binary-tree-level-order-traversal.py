# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        if root is None:
            return result
        
        current_depthNode = [root]
        while current_depthNode:
            result.append([curr.val for curr in current_depthNode])
            current_depthNode = [child for curr in current_depthNode for child in (curr.left, curr.right ) if child]
        return result
        