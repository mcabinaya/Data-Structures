# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.sol = []
        if root:
            self.levelOrderRecursive(root, 1)
        return self.sol
    
    def levelOrderRecursive(self, root, level):
        if len(self.sol) < level:
            self.sol.append([])
        self.sol[level-1].append(root.val)
        
        if root.left:
            self.levelOrderRecursive(root.left, level+1)
        if root.right:
            self.levelOrderRecursive(root.right, level+1)
