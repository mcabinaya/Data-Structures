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
        sol = []
        if root == None:
            return sol
        
        level_queue = [root]
        
        while len(level_queue) > 0:
            sol.append([i.val for i in level_queue])
            temp_queue = []
            
            while len(level_queue) > 0:
                node = level_queue.pop(0)
                
                if node.left != None:
                    temp_queue.append(node.left)

                if node.right != None:
                    temp_queue.append(node.right)
            
            level_queue = temp_queue
            
        return sol     
           
