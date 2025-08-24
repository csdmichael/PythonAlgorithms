from typing import List
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getRightView(self, root: TreeNode) -> List[int]:
        q = [root]
        res = []
        while len(q) > 0:
            qLen = len(q)
            for i in range(qLen):
                node = q.pop(0)
                if i == qLen - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return res

y = Solution().getRightView(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4))))
print(y)  # [1, 3, 4]