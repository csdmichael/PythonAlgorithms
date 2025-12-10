class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def findLCA(root: TreeNode, p: TreeNode, q: TreeNode)->TreeNode:
    if not root or p == root or q == root:
        return root
    left_lca = findLCA(root.left, p, q)
    right_lca = findLCA(root.right, p, q)

    if left_lca and right_lca:
        return root
    elif left_lca:
        return left_lca
    else:
        return right_lca

 
