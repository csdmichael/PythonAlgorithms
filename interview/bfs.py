from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val: int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root: TreeNode) -> List[int]:
    if root == None:
        return None
    q = deque([root])
    res = []
    while len(q) > 0:
        l = len(q)
        for i in range(l): #Go through nodes in current level
            currNode = q.popleft()
            res.append(currNode.val)
            #Add Children of current node
            if currNode.left:
                q.append(currNode.left)
            if currNode.right:
                q.append(currNode.right)
    return res

y = bfs(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(8, None, TreeNode(10))))
print(y)
