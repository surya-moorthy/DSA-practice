# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """    

        def helper(root , sum):

            if root is None:
                return 0
            
            curr = sum * 10 + root.val
            
            if not root.left and not root.right:
                return curr
            
            return helper(root.left, curr) + helper(root.right , curr)
        
        return helper(root, 0)
        