# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkDepth(self, p, q)-> bool:
        if not p and not q:
            return True        
        if not p or not q or (p.val != q.val):
            return False
        return self.checkDepth(p.left, q.left) and self.checkDepth(p.right, q.right)
            
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.checkDepth(p,q)
        
        