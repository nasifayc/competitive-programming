# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binarySearch(self,root,val):
        if not root:
            return None

        if root.val == val:
            return root
        elif root.val > val:
            return self.binarySearch(root.left, val)
        else:
           return self.binarySearch(root.right, val)

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.binarySearch(root,val)

        