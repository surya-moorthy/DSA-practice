# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.is_balanced = True

        def helper(root):

            if root is None:
                return 0

            left = helper(root.left)
            right = helper(root.right)

            if abs(left - right) > 1:
                self.is_balanced = False
            
            return max(left, right) + 1
        
        result = helper(root)

        return self.is_balanced