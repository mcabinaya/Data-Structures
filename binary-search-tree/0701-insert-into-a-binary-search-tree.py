# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # return a node if tree doesn't exist
        if root == None:
            return TreeNode(val)
        
        # track previous and current node, find the leaf node for insertion
        prev = root
        node = root
        
        while node != None:
            if val < node.val:
                prev = node
                node = node.left
            else:
                prev = node
                node = node.right
                
        # insert node        
        if val < prev.val: 
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)
         
        # return root node
        return root
        
                
        
        
