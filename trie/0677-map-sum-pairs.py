
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        node = self.root
        for w in key:
            if w not in node:
                node[w] = {}
            node = node[w]
        node["val"] = val

        
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        #print self.root
        
        node = self.root
        for p in prefix:
            if p not in node:
                return 0
            node = node[p]
       
        stack = []
        totSum = 0
        if "val" in node:
            totSum += node["val"]
            
        for key in node.keys():
            if key != "val":
                stack.append(node[key])
        
        while len(stack) > 0:
            child = stack.pop()
            if "val" in child:
                totSum += child["val"]
            for key in child.keys():
                if key != "val":
                    stack.append(child[key])
        
        return totSum
        
        
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
