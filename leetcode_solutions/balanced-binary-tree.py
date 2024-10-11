# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkDepth(self, root):
        if not root:
            return 0  

        left_depth = self.checkDepth(root.left)
        right_depth = self.checkDepth(root.right)
        
        if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
            return -1

        return max(left_depth, right_depth) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkDepth(root) != -1
