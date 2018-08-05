# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #set initial minimum and maximum value to compare
        min_val = -4294967296
        max_val = 4294967296
        return self.isValidBSTUtils(root, min_val, max_val)
    
    def isValidBSTUtils(self, node, min_val, max_val):
        # return if no node
        if node == None:
            return True
        
        # return false if binary search tree condition does not satisy
        if (node.val < min_val) or (node.val > max_val):
            return False
        
        # traverse left and right node recursively
        return self.isValidBSTUtils(node.left, min_val, node.val-1) & self.isValidBSTUtils(node.right, node.val+1, max_val)
        
