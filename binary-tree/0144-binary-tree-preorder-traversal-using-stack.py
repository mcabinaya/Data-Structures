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
        
        node = root
        stack = []
        sol = []
        
        while (len(stack) > 0) or (node != None):
            if node:
                sol.append(node.val)
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node = node.right
                
        return sol
