class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

def maxPathSum(root: 'TreeNode') -> int:
   max_sum = float('-inf')

   def dfs(node):
       nonlocal max_sum
       if not node:
           return 0

       left_sum = max(0, dfs(node.left))
       right_sum = max(0, dfs(node.right))

       # Path through the current node
       max_sum = max(max_sum, node.val + left_sum + right_sum)

       # Max path from current node to parent
       return node.val + max(left_sum, right_sum)

   dfs(root)
   return max_sum