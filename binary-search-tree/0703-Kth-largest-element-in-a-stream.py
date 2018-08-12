class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.count = 1

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.prevKthLargest = None
        self.root = None
        for val in nums:
            self.root = self.insertIntoBST(self.root, val)    

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.prevKthLargest == None:
            self.root = self.insertIntoBST(self.root, val) 
            KthLargest = self.getKthLargestVal(self.root, self.k)
            self.prevKthLargest = KthLargest
        else:
            if val < self.prevKthLargest:
                KthLargest = self.prevKthLargest

            else:
                self.root = self.deleteMinNode(self.root)
                self.root = self.insertIntoBST(self.root, val) 
                KthLargest = self.getKthLargestVal(self.root, self.k)
                self.prevKthLargest = KthLargest
    
        return KthLargest
    
    def deleteMinNode(self, root):
        if root.left is not None:
            root.left = self.deleteMinNode(root.left)
            return root
        else:
            return root.right
        
    def insertIntoBST(self, root, val):
        if root == None:
            return TreeNode(val)
        
        prev = root
        node = root
        
        while node != None:
            if val < node.val:
                prev = node
                node.count += 1
                node = node.left
            else:
                prev = node
                node.count += 1
                node = node.right
                
        if val < prev.val: 
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)
            
        return root
        
    def getKthLargestVal(self, root, k):
        right_count = root.right.count if root.right!= None else 0
        newk = k - right_count - 1
        if newk > 0:
            val = self.getKthLargestVal(root.left, newk)
        elif newk < 0:
            val = self.getKthLargestVal(root.right, k)
        else: 
            val = root.val
        return val
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
