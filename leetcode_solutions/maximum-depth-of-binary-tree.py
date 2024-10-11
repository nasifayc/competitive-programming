# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkDepth(self,root, count):
        if not root:
            return count
        left = self.checkDepth(root.left, count + 1)
        right = self.checkDepth(root.right, count + 1)
        return max(left,right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.checkDepth(root,0)
