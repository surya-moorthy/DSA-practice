# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        ans = []
        lst = []
        self.traverse(root, targetSum, 0, lst, ans)
        return ans
    
    def traverse(self, root, targetSum, sum, lst, ans):
        if root is None:
            return
        
        if not root.left and not root.right:
            sum += root.val
            lst.append(root.val)
            
            if targetSum == sum:
                ans.append(lst)
            
            return
        
        sum += root.val
        lst.append(root.val)
        self.traverse(root.left, targetSum , sum, lst[:], ans)
        self.traverse(root.right, targetSum , sum, lst[:], ans)
    