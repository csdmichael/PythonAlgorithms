class TreeNode:
    def __init__(self, value: int, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def dfs(self, node : TreeNode)->int:
        if not node:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.diameter = max([self.diameter, left + right])
        return 1 + max([left, right])
    
    def getTreeDiameter(self, root: TreeNode)->int:
        self.diameter = 0
        self.dfs(root)
        return self.diameter


'''
            5
        /      \\
       3         7
     /   \       
    1     4    

'''

n1 = TreeNode(1)
n4 = TreeNode(4)
n3 = TreeNode(3, n1, n4)
n7 = TreeNode(7)
root = TreeNode(5, n3, n7)

s = Solution()
y = s.getTreeDiameter(root)
print(y)