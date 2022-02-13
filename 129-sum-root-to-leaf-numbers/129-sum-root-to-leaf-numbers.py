# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def rootToLeafHelper(currentNode, countingSum):
            if currentNode == None:
                return 0
            
            countingSum = countingSum * 10 + currentNode.val
            
            if currentNode.left == None and currentNode.right == None:
                return countingSum 
            else:
                return (rootToLeafHelper(currentNode.left, countingSum)) +  (rootToLeafHelper(currentNode.right, countingSum))
            
            
        return rootToLeafHelper(root, 0)
        
                