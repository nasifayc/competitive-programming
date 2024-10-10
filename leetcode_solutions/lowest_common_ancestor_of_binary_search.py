# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binarySearch(self,root,left, right):
        if not root:
            return None

        if root.val > left.val and root.val > right.val:
            return self.binarySearch(root.left, left, right)
        elif root.val < left.val and root.val < right.val:
            return self.binarySearch(root.right, left, right)
        else:
           return root
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.binarySearch(root,p,q)
        