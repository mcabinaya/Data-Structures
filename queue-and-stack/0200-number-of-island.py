class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        queue = []
        num_islands = 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1': #first node of a group
                    queue.append([i,j])
                    num_islands += 1
                    
                    #all nodes connected to the group will be visited and marked '0'
                    while len(queue) > 0:
                        [temp_row,temp_col] = queue.pop(0)
                        if grid[temp_row][temp_col] == '1': #if not visited
                            # append surrounding nodes with "1"
                            if temp_row-1 >= 0 : 
                                if grid[temp_row-1][temp_col] == "1":
                                    queue.append([temp_row-1, temp_col])
                            if temp_col-1 >= 0:
                                if grid[temp_row][temp_col-1] == "1":
                                    queue.append([temp_row, temp_col-1])
                            if temp_row+1 < row :
                                if grid[temp_row+1][temp_col] == "1":
                                    #print temp_row+1, temp_col
                                    queue.append([temp_row+1, temp_col])
                            if temp_col+1 < col:
                                if grid[temp_row][temp_col+1] == "1":
                                    #print temp_row, temp_col+1
                                    queue.append([temp_row, temp_col+1])

                        grid[temp_row][temp_col] = '0' #not to be visited again
        return num_islands

                
                            
                
                
                
        
        
        
        
