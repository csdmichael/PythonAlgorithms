from typing import List

class TreeNode:
    def __init__(self, val: int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class TreeTraversals:
    def inOrder(self, root) -> List[int]:
        if root == None:
            return []
        left = []
        right = []
        if root.left != None:
            left = self.inOrder(self, root.left)
        
        if root.right != None:
            right = self.inOrder(self, root.right)
        
        return left + [root.val] + right

t = TreeNode(5, TreeNode(3), TreeNode(7, TreeNode(6), TreeNode(8)))
res = TreeTraversals.inOrder(TreeTraversals, t)
print(res)