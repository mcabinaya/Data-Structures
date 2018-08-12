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
        # ensure p < q
        if p.val > q.val:
            p, q = q, p

        if root == None:
            return None 
        
        if (root.val < p.val) & (root.val < q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        
        if (root.val > p.val) & (root.val > q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        
        # return if value is between p and q or equal to something
        return root
