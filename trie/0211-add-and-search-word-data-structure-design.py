class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]
        node["isword"] = "True" 
              

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        #print self.root
        stack = [self.root]
        i = 0
        while (i < len(word)) & (len(stack) > 0):
            
            temp_stack = []
            while len(stack) > 0:
                node = stack.pop()

                if word[i] == ".":
                    for ch in node:
                        if ch != "isword":
                            temp_stack.append(node[ch])
                elif word[i] in node:
                    temp_stack.append(node[word[i]])
                #print word[i], temp_stack
                
            stack = temp_stack[:]
            i += 1
        
        if (i == len(word)) & (any("isword" in node for node in stack)):
            return True
        else:
            return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
