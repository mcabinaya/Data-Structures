# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.sol = []
        self.postorderRecursive(root)
        return self.sol
    
    def postorderRecursive(self, root):
        if root == None:
            return None
        self.postorderRecursive(root.left)
        self.postorderRecursive(root.right)
        self.sol.append(root.val)
               
