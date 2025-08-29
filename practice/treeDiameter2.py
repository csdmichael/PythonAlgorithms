class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    diameter: int = 0
    def getTreeDiameter(self, root: TreeNode) -> int:
        
        def dfs(self, root: TreeNode) -> int:
            if root == None:
                return 0
            
            left = dfs(self, root.left)
            right = dfs(self, root.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        
        dfs(self, root)
        return self.diameter
    
y = Solution.getTreeDiameter(Solution, TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(8)))
print(y)