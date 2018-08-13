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
        node = root
        stack = []
        sol = []
        
        while (len(stack) > 0) or (node != None):
            if node:
                if node.right != None:
                    stack.append(node.right)
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if (node.right != None) & (node.right == self.returnLastStackVal(stack)):
                    stack.pop()
                    stack.append(node)
                    node = node.right
                else:
                    sol.append(node.val)
                    node = None

        return sol 
    
    def returnLastStackVal(self, stack):
        if len(stack) > 0:
            return stack[-1]
        return None
