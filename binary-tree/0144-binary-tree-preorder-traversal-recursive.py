# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.sol = []
        self.preorderRecursive(root)
        return self.sol
    
    def preorderRecursive(self, root):
        if root == None:
            return None
        self.sol.append(root.val)
        self.preorderRecursive(root.left)
        self.preorderRecursive(root.right)
        
