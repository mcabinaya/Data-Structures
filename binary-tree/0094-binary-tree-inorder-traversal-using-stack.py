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
        node = root
        stack = []
        sol = []
        
        while (len(stack) > 0) or (node != None):
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                sol.append(node.val)
                node = node.right
                
        return sol 
