from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def DisplayTreeLeftView(root) -> list:
        if not root:
            return []
        
        rvNodes = []
        queue = deque([root])

        # BFS Traverse tree using queue
        while (len(queue) > 0):
            l = len(queue)
            print(l)
            #Iterate over current level
            for i in range(l):
                curr = queue.popleft()
                if (curr.left):
                    queue.append(curr.left)
                if (curr.right):
                    queue.append(curr.right)

            # Add last element of current level to result list
            rvNodes.append(curr.val)
        return rvNodes

t = TreeNode(5)
t.left = TreeNode(3)
t.right = TreeNode(7)
t.left.left = TreeNode(1)
t.left.right = TreeNode(4)

#                   5
#          3                7
#      1        4

result = DisplayTreeLeftView(t)
print(result)