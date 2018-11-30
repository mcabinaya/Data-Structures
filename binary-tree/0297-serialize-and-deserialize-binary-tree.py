# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        
        serialized = []
        queue = [root]
        
        while len(queue) > 0:
            node = queue.pop(0)

            if node:
                serialized.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            
            else:
                serialized.append("null")

        return ",".join(serialized)      

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(",")
        
        
        element = data.pop(0)
        root = TreeNode(element)  
        previous_level= [root]
        
        level_len = 2
        
        while len(data) > 0:
            
            previous_level_temp = []
            
            while len(previous_level) > 0:
                
                previous_node = previous_level.pop(0)
                if previous_node == "null":
                    continue
                
                element_left = data.pop(0)
                element_right = data.pop(0)
                if element_left != "null":
                    previous_node.left = TreeNode(element_left)
                    previous_level_temp.append(previous_node.left)
                else:
                    previous_level_temp.append("null")
                    
                if element_right != "null":
                    previous_node.right = TreeNode(element_right)
                    previous_level_temp.append(previous_node.right)
                else:
                    previous_level_temp.append("null")
 
            previous_level = previous_level_temp[:]
            level_len = level_len * 2
        
        return root
            
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
