# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        # using bfs
        queue = [root]  
        result = []
        reverse_flag = 0
        while(len(queue) >0):            
            present_size = len(queue)                               
            temp_result = []
            for i in range(present_size):  # nodes at every level       
                element = queue.pop(0)
                temp_result.append(element.val)
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            if reverse_flag:
                result.append(temp_result[::-1])
                reverse_flag = 0
            else:
                result.append(temp_result)
                reverse_flag = 1
        return result



        
