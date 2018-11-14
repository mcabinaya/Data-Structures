class Solution(object):
    def insert(self, word, root):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = root
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]
        node["isword"] = "True" 
        return root
    
    def search(self, row, col, m, n, root, visited, result, myStr, board):
        #print row, col, visited, root
        
        if "isword" in root:
            #print myStr
            result.add(myStr)
            
        if visited[row][col] == '0': #if not visited before
            visited[row][col] = '1' #make it visited
            
            for ch in root:
                if ch != "isword":
                    if row-1 >= 0:
                        if (board[row-1][col] == ch) and (visited[row-1][col] != '1'):
                            self.search(row-1, col, m, n, root[ch], visited, result, myStr+ch, board) 

                    if col-1 >= 0:
                        if (board[row][col-1] == ch) and ( visited[row][col-1] != '1'):
                            self.search(row, col-1, m, n, root[ch], visited, result, myStr+ch, board)

                    if row+1 < m:
                        if (board[row+1][col] == ch) and (visited[row+1][col] != '1'):
                            self.search(row+1, col, m, n, root[ch], visited, result, myStr+ch, board)

                    if col+1 < n:
                        if (board[row][col+1] == ch) and (visited[row][col+1] != '1'):
                            self.search(row, col+1, m, n, root[ch], visited, result, myStr+ch, board)
        
        myStr = myStr[:-1]
        visited[row][col] = '0'      
        
     
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m = len(board)
        n = len(board[0])
        
        root = {}
        for word in words:
            root = self.insert(word, root)
        
        visited = [['0']*n for _ in range(m)]
        result = set([])
        
        for row in range(m):
            for col in range(n):
                if board[row][col] in root:
                    self.search(row, col, m, n, root[board[row][col]], visited, result, board[row][col], board)
        return list(result)

