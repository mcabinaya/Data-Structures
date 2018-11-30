"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
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
        
        for child in root.children:
            self.levelOrderRecursive(child, level+1)
        
            
        
