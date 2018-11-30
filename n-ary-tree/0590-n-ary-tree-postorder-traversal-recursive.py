"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.sol = []
        self.postorderRecursive(root)
        return self.sol
    
    def postorderRecursive(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return None
        
        for child in root.children:
            self.postorderRecursive(child)
        
        self.sol.append(root.val)
        
