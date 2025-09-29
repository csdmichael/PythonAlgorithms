from collections import deque

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getTreeRightView(root: TreeNode)-> list:
        if root == None:
            return []
        rvRes = []
        queue = deque([root])
        while len(queue) > 0:
            cnt = len(queue)
            for i in range(cnt):
                currNode = queue.popleft()
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            rvRes.append(currNode.val)
        return rvRes
    
t = TreeNode(5)
t.left = TreeNode(3)
t.right = TreeNode(7)
t.left.left = TreeNode(1)
t.left.right = TreeNode(4)

#                   5
#          3                7
#      1        4

s = Solution 
result = s.getTreeRightView(t)
print(result)
                