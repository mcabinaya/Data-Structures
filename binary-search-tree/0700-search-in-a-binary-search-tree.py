# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        #similar to binary search in an array
        node = root
        while node != None:
            if node.val == val:
                return node
            elif node.val < val:
                node = node.right
            else:
                node = node.left
                
        return None
