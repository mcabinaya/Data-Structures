class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
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
            
        result = [[0]*(i+1) for i in range(numRows)]
        self.cache = {}
        for row in range(1,numRows+1):
            for col in range(1,row+1):
                result[row-1][col-1] = generateUtils(row, col)
        return result     
        

                
        
