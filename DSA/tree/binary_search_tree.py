class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

class BinarySearchTree:
    def insert(self,root, val):
        if not root:
            return TreeNode(val)
        else:
            if val > root.value:
                root.right = self.insert(root.right, val)
            elif val < root.value:
                root.left = self.insert(root.left, val)
        return root
    def inorder(self,root):

        if not root:
            return
        self.inorder(root.left)
        print(root.value, end=' ')
        self.inorder(root.right)
    
    def preorder(self,root):

        if not root:
            return
        print(root.value, end=' ')
        self.preorder(root.left)
        self.preorder(root.right)
    def postorder(self,root):

        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.value, end=' ')

if __name__ == "__main__":
    bst = BinarySearchTree()
    root = None
    root = bst.insert(root, 50)
    bst.insert(root, 30)
    bst.insert(root, 20)
    bst.insert(root, 40)
    bst.insert(root, 70)
    bst.insert(root, 60)
    bst.insert(root, 80)
    print("Inorder traversal:")
    bst.inorder(root)
    print("\nPreorder traversal:")
    bst.preorder(root)
    print("\nPostorder traversal:")
    bst.postorder(root)