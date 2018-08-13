# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.sol = []
        self.inorderRecursive(root)
        return self.sol
    
    def inorderRecursive(self, root):
        if root == None:
            return None
        self.inorderRecursive(root.left)
        self.sol.append(root.val)
        self.inorderRecursive(root.right)
       
