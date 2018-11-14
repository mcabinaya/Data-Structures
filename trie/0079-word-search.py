class Solution(object):
    def search(self, row, col, m, n, visited, board, word):
        #print row, col, visited, word
        if len(word) == 0:
            return True
        elif len(word) == 1:
            if board[row][col] == word[0]:
                return True
        
        if board[row][col] == word[0]:
            visited[row][col] = '1'
            if row-1 >= 0:
                if visited[row-1][col] != '1':
                    if self.search(row-1, col, m, n, visited, board, word[1:]):
                        return True
            if col-1 >= 0:
                if visited[row][col-1] != '1':
                    if self.search(row, col-1, m, n, visited, board, word[1:]):
                        return True
            if row+1 < m:
                if visited[row+1][col] != '1':
                    if self.search(row+1, col, m, n, visited, board, word[1:]):
                        return True
            if col+1 < n:
                if visited[row][col+1] != '1':
                    if self.search(row, col+1, m, n, visited, board, word[1:]):
                        return True
            visited[row][col] = '0'
        return False  
        
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        visited = [['0']*n for _ in range(m)]
        for row in range(0, m):
            for col in range(0, n):
                #if board[row][col] == word[0]:
                if self.search(row, col, m, n, visited, board, word):
                    return True
                
        return False
                    
                


                    
        
        
