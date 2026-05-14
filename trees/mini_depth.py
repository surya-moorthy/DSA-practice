from collections import deque

def helper_dfs_approach(root):
    if root is None:
        return 0
    if root.left is None:
        return 1 + helper_dfs_approach(root.right)
    
    if root.right is None:
        return 1 + helper_dfs_approach(root.left)

    return 1 + min(helper_dfs_approach(root.left), helper_dfs_approach(root.right))

def helper_bfs_approach(root):
    q = deque()
    q.append([root,1])

    while q:
        curr, depth = q.popleft()

        if curr.left is None and curr.right is None:
            return depth
        
        if curr.left:
            q.append([curr.left, depth + 1])

        if curr.right:
            q.append([curr.right, depth + 1])