class Solution(object):
    
    def floodFillUtils(self, image, row, col, newColor, oldColor, m, n, visited):
        
        if visited[row][col] != 1:
            if image[row][col] == oldColor:
                image[row][col] = newColor
                visited[row][col] = 1

                if row-1 >= 0:
                    image = self.floodFillUtils(image, row-1, col, newColor, oldColor, m, n, visited)
                if col-1 >= 0:
                    image = self.floodFillUtils(image, row, col-1, newColor, oldColor, m, n, visited)
                if row+1 < m:
                    image = self.floodFillUtils(image, row+1, col, newColor, oldColor, m, n, visited)
                if col+1 < n:
                    image = self.floodFillUtils(image, row, col+1, newColor, oldColor, m, n, visited)
                
        return image
    
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m = len(image)
        n = len(image[0])
        
        visited = [[0]*n for _ in range(m)]
        
        oldColor = image[sr][sc]
        image = self.floodFillUtils(image, sr, sc, newColor, oldColor, m, n, visited)
        
        return image
        
