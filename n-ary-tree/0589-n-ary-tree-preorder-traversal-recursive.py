"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.sol = []
        self.preorderRecursive(root)
        return self.sol
    
    def preorderRecursive(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return None
        
        self.sol.append(root.val)
        for child in root.children:
            self.preorderRecursive(child)
        
