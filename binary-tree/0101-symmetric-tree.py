# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        return self.isSymmetricUtils(root.left, root.right)
        
    def isSymmetricUtils(self, left, right):
        #recurse until leaf nodes: if both are None return True
        if (left == None) and (right == None):
            return True
        
        #recurse until leaf nodes: if one is None other is not, return False
        if (left == None) or (right == None):
            return False
        
        #check for three conditions and recurse
        check1 = left.val == right.val
        
        if check1 == False:
            return False
        
        else:
            check2 = self.isSymmetricUtils(left.left, right.right)
            check3 = self.isSymmetricUtils(left.right, right.left)
            return (check2 & check3)
