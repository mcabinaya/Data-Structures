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
        sol = []
        stack = [root]
        
        while len(stack) > 0:
            node = stack.pop()
            if node is not None:
                sol.append(node.val)
            
                for child in node.children[::-1]:
                    stack.append(child)

        return sol
