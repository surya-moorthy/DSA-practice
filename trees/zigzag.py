from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def helper(root):
    if root is None:
        return []
    
    lst = []
    depth = 1

    q = deque()
    q.append(root)

    while q:
        size = len(q)

        if len(lst) < depth:
            lst.append([])

        for i in range(size):
            cur = q.popleft()

            lst[depth - 1].append(cur.val)

            if depth % 2 != 0:
                if cur.right is not None:
                    q.append(cur.right)
                    
                if cur.left is not None:
                    q.append(cur.left)
            else:
                if cur.left is not None:
                    q.append(cur.right)
                    
                if cur.right is not None:
                    q.append(cur.left)
        depth += 1
    return lst

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.left = TreeNode(6)
node.right.right = TreeNode(7)

print(helper(node))