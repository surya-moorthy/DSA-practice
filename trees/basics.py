class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

preOrderTraversal = []
inOrderTraversal = []
PostOrderTraversal = []
    
def traverse(node : Tree):
    if node is None:
        return
    
    preOrderTraversal.append(node.val)
    traverse(node.left)

    inOrderTraversal.append(node.val)
    traverse(node.right)

    PostOrderTraversal.append(node.val)
        

node = Tree(1)
node.left = Tree(2)
node.right = Tree(3)
node.left.left = Tree(4)
node.left.right = Tree(5)
node.right.left = Tree(6)
node.right.right = Tree(7)

traverse(node)

print(preOrderTraversal)
print(inOrderTraversal)
print(PostOrderTraversal)