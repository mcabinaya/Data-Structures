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
        if root is None:
            return []
        queue = [root]
        sol = []
        
        while len(queue) > 0:
            temp_sol = []
            level_len = len(queue)
            
            for i in range(level_len):
                node = queue.pop(0)
                temp_sol.append(node.val)
                for child in node.children:
                    queue.append(child)
            
            sol.append(temp_sol)
    
        return sol
        
        
