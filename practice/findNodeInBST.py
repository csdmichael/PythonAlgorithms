class TreeNode:
    def __init__(self, val: int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findNode(self, root: TreeNode, x: int) -> bool:
        if root == None:
            return False
        ptr = root
        while ptr != None:
            if ptr.val == x:
                return True
            else:
                if x < ptr.val:
                    ptr = ptr.left
                else:
                    ptr = ptr.right
        return False

y = Solution().findNode( TreeNode(5, TreeNode(3, TreeNode(2)), TreeNode(8)), 9)
print(y)