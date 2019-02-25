class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # using recursing with memorization
        def generateUtils(row, col):
            if (col == 1) or (row == col):
                return 1
            if (row, col) in self.cache:
                return self.cache[(row,col)]
            value = generateUtils(row-1, col-1) + generateUtils(row-1, col)
            self.cache[row,col] = value
            return value
            
        result = [0]*(rowIndex+1)
        self.cache = {}
        for col in range(1,rowIndex+2):
            result[col-1] = generateUtils(rowIndex+1, col)
        return result     
                
