# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        #recursive solution
        if inorder:
            element = preorder.pop(0) #pop first element from preorder
            inIndex = inorder.index(element) #find the element in inorder
            root = TreeNode(element)
            root.left = self.buildTree(preorder, inorder[:inIndex]) #recurse to form left sub tree
            root.right = self.buildTree(preorder, inorder[inIndex+1:]) #recurse to form right sub tree
            return root

