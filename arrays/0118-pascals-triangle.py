class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            result = [[1],[1,1]]
            for row in range(1,numRows-1):
                #print "row--- ", row
                temp_result = [1,1]
                temp_result = temp_result[:1] + ([0]*(row)) + temp_result[:-1]
                for i in range(int(round(row/float(2)))):
                    #print "---", i+1
                    temp_result[i+1] = result[row][i]+result[row][i+1]
                    another_i = (row+1) - (i+1)
                    if another_i != (i+1):
                        #print (i+1), another_i, result[row][i]+result[row][i+1]
                        temp_result[another_i] = result[row][i]+result[row][i+1]
                    #print temp_result
                #print temp_result
                result.append(temp_result)
            return result
                




        
