# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root == None:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        else:
            if root.left == None:
                temp = root.right
                root = None
                return temp
            
            elif root.right == None:
                temp = root.left
                root = None
                return temp
            
            else:
                temp = self.getMinValueNode(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
        
        return root
                
    def getMinValueNode(self, root):
        curr = root
        while curr.left != None:
            curr = curr.left
        return curr
