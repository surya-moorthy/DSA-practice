from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[List[int]]
    """

    result : list[list[int]] = helper(root)

    print(result)

def helper(root : TreeNode):
    if root is None:
        return []
    
    q = deque()
    q.append(root)

    lst : list[list[int]] = []
    depth = 1

    while q:
        size = len(q)

        if len(lst) < depth:
            lst.append([])

        for i in range(size):
            cur : TreeNode = q.popleft()

            lst[depth - 1].append(cur.val)

            if cur.left is not None:
                q.append(cur.left)

            if cur.right is not None:
                q.append(cur.right)
        
        depth += 1
    
    return lst

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.left = TreeNode(6)
node.right.right = TreeNode(7)

levelOrder(node)