# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchTree(self,root, arr, target):
        if not root:
            return False
        if not root.left and not root.right:
            arr.append(root.val)
            if sum(arr) == target:
                return True
            else:
                arr.pop()
                return False

        arr.append(root.val)
        if self.searchTree(root.left, arr, target):
            return True
        if self.searchTree(root.right, arr, target):
            return True
        arr.pop()
        return False
       
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        arr = []
        return self.searchTree(root,arr,targetSum)

        
        
        