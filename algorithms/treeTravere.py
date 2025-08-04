class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class TreeTraversals:
    def inorder(self, root: TreeNode) -> list:
        if (root == None):
            return []
        left = []
        right = []
        if (root.left != None):
            left = self.inorder(self, root.left)
        if (root.right != None):
            right = self.inorder(self, root.right)
        return left + [root.val] + right
    
    def preorder(self, root: TreeNode) -> list:
        if (root == None):
            return []
        left = []
        right = []
        if (root.left != None):
            left = self.preorder(self, root.left)
        if (root.right != None):
            right = self.preorder(self, root.right)
        return [root.val] + left + right
    
        
    def postorder(self, root: TreeNode) -> list:
        if (root == None):
            return []
        left = []
        right = []
        if (root.left != None):
            left = self.postorder(self, root.left)
        if (root.right != None):
            right = self.postorder(self, root.right)
        return left + right + [root.val]
    
i = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(8, None, TreeNode(10)))
y = TreeTraversals.inorder(TreeTraversals, i)
print("In-Order", y)


y = TreeTraversals.preorder(TreeTraversals, i)
print("Pre-Order", y)


y = TreeTraversals.postorder(TreeTraversals, i)
print("Post-Order", y)