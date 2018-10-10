# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        node = root
        stack = []
        temp_k = 0
        
        #inorder traversal of tree will sort
        while (len(stack)>0) or (node!= None):
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                temp_k+= 1
                if temp_k == k:
                    return node.val #return when k values are found in inorder
                node = node.right

