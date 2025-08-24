from typing import Optional

class TreeNode:
    def __init__(self, val: int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    diameter = 0
    def getTreeDiameter(self, root: Optional[TreeNode]) -> int:
       
        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.diameter
        
t = TreeNode(5, TreeNode(3), TreeNode(7, TreeNode(6), TreeNode(8)))
res = Solution.getTreeDiameter(Solution, t)
print(res)
