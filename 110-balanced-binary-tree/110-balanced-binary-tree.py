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
            # i.e If there is no tree at all
            if not root:
                #An empty tree is a balanced tree.
                return BalancedStatusWithHeight(balanced= True, height = -1)
         
            leftChild_check = check_balanced(root.left)
            #if left child is not balanced, return the left child
            if not leftChild_check.balanced:
                return leftChild_check
            
            rightChild_check = check_balanced(root.right)
            #if right child is not balanced, return the right child
            if not rightChild_check.balanced:
                return rightChild_check
            
            #returns a truthy value
            #Adding 1 to the max of the left and right child is standard formula to find the max height of a subtree
            height = max(leftChild_check.height, rightChild_check.height) + 1
              # a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
            isBalanced = abs(leftChild_check.height - rightChild_check.height) <= 1
        
            return BalancedStatusWithHeight(isBalanced, height)
        #RECURSION checks if the current stack returns true of false.
        return check_balanced(root).balanced
            
        