class TreeNode:
    def __init__(self, val: int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def findLCA(root: TreeNode, p: TreeNode, q: TreeNode)->TreeNode:
    if not root or root == p or root == q:
        return root
    left_lca = findLCA(root.left, p, q)
    right_lca = findLCA(root.right, p, q)

    if left_lca and right_lca:
        return root
    elif left_lca:
        return left_lca
    else:
        right_lca


'''
      5
    /   \
   3     7
  / \     \
 1   4     9
            \
            10

 Root = 5
 p = 3
 q = 4

 left_lca = 3
 right_lca = None

 3


Root = 5
 p = 9
 q = 10
'''

n1 = TreeNode(1)
n4 = TreeNode(4)
n3 = TreeNode(3, n1, n4)
n10 = TreeNode(10)
n9 = TreeNode(9, None, n10)
n7 = TreeNode(7, None, n9)
root = TreeNode(5, n3, n7)

y = findLCA(root, n3, n9)

print(y.val)
