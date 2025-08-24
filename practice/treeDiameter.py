from typing import Optional

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    diameter = 0
    def getBreadth(self, root: Optional[TreeNode]) -> int:
        def dfs(self, root) -> int:
            if root == None:
                return 0 #height
            left = dfs(self, root.left)
            right = dfs(self, root.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        dfs(self, root)
        return self.diameter