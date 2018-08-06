# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.bst_list = []
        self.i = 0
        self.inorder(root)
        
    def inorder(self, node):
        if node != None:
            self.inorder(node.left)
            self.bst_list.append(node.val)
            self.inorder(node.right)          

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.i < len(self.bst_list) else False
        
    def next(self):
        """
        :rtype: int
        """
        val = self.bst_list[self.i]
        self.i += 1
        return val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
