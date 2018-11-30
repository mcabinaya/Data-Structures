# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        
        return self.hasPathSumUtils(root, sum)
    
    def hasPathSumUtils(self, node, sum):
        
        if node == None:
            return False
        
        sum -= node.val
        
        if (node.left == None) & (node.right == None):
            return sum==0
        
        check1 = self.hasPathSumUtils(node.left, sum)
        check2 = self.hasPathSumUtils(node.right, sum)
        
        if check1 or check2:
            return True
        
        return False
