from typing import Optional
from collections import deque
import json
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #Level Traverse Tree
        if root is None:
            return 0
        minLevels = 0
        queue = deque([root])
        while len(queue) > 0:
            minLevels += 1
            l = len(queue)
            for i in range(l):
                curr = queue.popleft()
                #Check if leaf node
                if curr.left == None and curr.right == None:
                    return minLevels
                else:
                    if curr.left != None:
                        queue.append(curr.left)
                    if curr.right != None:
                        queue.append(curr.right)
        return minLevels
    
x = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
y = Solution.minDepth(Solution, x)

print(y)