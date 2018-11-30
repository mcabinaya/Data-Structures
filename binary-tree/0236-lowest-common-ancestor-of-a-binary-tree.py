# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #base case
        if root == None: 
            return None
        
        #find the node either with p or q value
        if (root.val == p.val) or (root.val == q.val): 
            return root
        
        #check for left and right subtree for p and q value
        left_check = self.lowestCommonAncestor(root.left, p, q)
        right_check = self.lowestCommonAncestor(root.right, p, q)
        
        #if both the values are present in the left and right subtree return the node as lca
        if left_check and right_check:
            return root
        
        #if one value is present, return the node with the value
        if left_check is not None:
            return left_check
        else:
            return right_check
        
