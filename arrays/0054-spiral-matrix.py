class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row = len(matrix)
        col = 0 if row == 0 else len(matrix[0])
        row_start = 0
        col_start = 0
        row_end = row-1
        col_end = col-1
        
        result = []
        while ((row_start<=row_end) and (col_start<=col_end)):
            for j in range(col_start, col_end+1):
                result.append(matrix[row_start][j])
            for i in range(row_start+1, row_end+1):
                result.append(matrix[i][col_end])
            if row_start != row_end:
                for j in range(col_end-1, col_start-1, -1):
                    result.append(matrix[row_end][j])
            if col_start != col_end:            
                for i in range(row_end-1, row_start-1+1, -1):
                    result.append(matrix[i][col_start])
            row_start += 1
            col_start += 1
            row_end -= 1
            col_end -= 1
        return result
