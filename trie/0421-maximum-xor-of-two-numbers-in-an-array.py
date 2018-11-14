class Solution(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}  

    def insert(self, num):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in range(31,-1,-1):
            bit = (num >> i) & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]
        node["val"] = num
    
    def findPresentMax(self, num):
        node = self.root
        xor = 0
        for i in range(31,-1,-1):
            bit = (num >> i) & 1
            #print bit, node
            if (0 in node) & (1 in node):
                if bit:
                    node = node[0]
                else:
                    node = node[1]
                xor += 1 << i
            
            else: 
                if 0 in node:
                    if bit == 1:
                        xor += 1 << i
                    node = node[0]
                elif 1 in node:
                    if bit == 0:
                        xor += 1 << i
                    node = node[1]
                
        return node["val"], xor
                    
    
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum1 = nums[0]
        maxnum2 = nums[0]
        maxxor = 0
        self.insert(nums[0])
                
        for i in range(1, len(nums)):
            tempmaxnum1, tempmaxxor = self.findPresentMax(nums[i])
            if tempmaxxor > maxxor:
                maxnum1 = tempmaxnum1
                maxnum2 = nums[i]
                maxxor = tempmaxxor
            
            self.insert(nums[i])
        
        #print "pair: ", maxnum1, maxnum2
        return maxxor
        
