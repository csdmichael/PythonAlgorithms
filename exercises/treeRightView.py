from collections import deque

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def getTreeRightView(root: TreeNode) -> list[int]:
    if not root:
        return []
    
    res = []
    q = deque([root])

    while len(q) > 0:
        l = len(q)
        # Process current level
        print(f"New Level - Len = : {l}")
        for i in range(l):
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        res.append(curr.val)
        print(f'Added: {curr.val}')
    return res

input = TreeNode(5)
input.left = TreeNode(3, TreeNode(1), TreeNode(4))
input.right = TreeNode(8, TreeNode(6))

ans = getTreeRightView(input)
print(ans)




