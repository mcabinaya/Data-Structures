# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root != None:
            
            # using bfs
            queue = [root]  
            
            while(len(queue) >0):            
                present_size = len(queue)           
                
                # nodes at every level
                for i in range(present_size):           
                    element = queue.pop(0)

                    if i < present_size-1:
                        element.next = queue[0] # point to the next node in that level
                    else:
                        element.next = None # if rightmost node, point to None

                    if element.left:
                        queue.append(element.left)
                    if element.right:
                        queue.append(element.right)


            
        
        
        
