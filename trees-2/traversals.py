from collections import deque

class Treenode:
    val = 0
    left = None
    right = None

    def __init__(self, val, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
        

def preorder(node : Treenode):
    if not node:
        return
    
    print(node.val)
    preorder(node.left)
    preorder(node.right)

def inorder(node : Treenode):
    if not node:
        return
    
    preorder(node.left)
    print(node.val)
    preorder(node.right)

def postorder(node : Treenode):
    if not node:
        return
    
    postorder(node.left)
    postorder(node.right)
    print(node.val)

def levelorder(root : Treenode):

    if not root:
        return
    
    q = deque()
    q.append(root)

    while(q) :
        size  = len(q)
        for i in range(size):
            node = q.popleft()

            print(node.val)

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

def height(root : Treenode):
    if not root:
        return 0
    
    left = height(root.left)
    right = height(root.right)

    return 1 + max(left, right)
