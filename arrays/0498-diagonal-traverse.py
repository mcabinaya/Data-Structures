class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row = len(matrix)
        col = 0 if row == 0 else len(matrix[0])
        result = []
        uphill = 1
        for temp_sum in range(row+col-1):
            temp_result = []
            #print("------------------",temp_sum)
            i_start = temp_sum if temp_sum <= (row-1) else (row-1)
            for i in range(i_start,-1,-1):
                j = temp_sum - i
                #print("---",i,j)
                if j <= (col-1):
                    #print("-Used")
                    temp_result.append(matrix[i][j])
                else:
                    break
            if uphill == 1:
                result = result + temp_result
                uphill = 0
            else:
                result = result + temp_result[::-1]
                uphill = 1
        return result
              
            
            
            
        
