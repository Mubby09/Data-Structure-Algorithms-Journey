# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkSym(subtreeOne, subtreeTwo):
            if not subtreeOne and not subtreeTwo:
                # If the root has no subtree, then it mirrors itself, hence, the tree is symmetric
                return True
            
            elif subtreeOne and subtreeTwo:
                return (subtreeOne.val == subtreeTwo.val and 
                       checkSym(subtreeOne.left, subtreeTwo.right) and checkSym(subtreeOne.right, subtreeTwo.left))
            return False
        
        return not root or checkSym(root.left, root.right)
            
            
            