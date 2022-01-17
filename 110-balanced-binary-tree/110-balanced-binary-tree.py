# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))
        
        def check_balanced(root):
            if not root:
                return BalancedStatusWithHeight(balanced= True, height = -1)
         
            leftChild_check = check_balanced(root.left)
            if not leftChild_check.balanced:
                return leftChild_check
            
            rightChild_check = check_balanced(root.right)
            if not rightChild_check.balanced:
                return rightChild_check
            
            # a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
            isBalanced = abs(leftChild_check.height - rightChild_check.height) <= 1
            height = max(leftChild_check.height, rightChild_check.height) + 1
        
            return BalancedStatusWithHeight(isBalanced, height)
    
        return check_balanced(root).balanced
            
        