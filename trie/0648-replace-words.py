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
    
    def createTrie(self, words):
        root = {}
        for word in words:
            root = self.insert(word, root)
        return root
    
    def searchRequired(self, word, root):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = root
        returnStr = ""
        for w in word:
            returnStr = returnStr + w
            if w not in node:
                return ""
            else:
                if "isword" in node[w]:
                    return returnStr
                node = node[w]
        return ""
        
        
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        root = self.createTrie(dict)
        sentenceWords = sentence.split()
        
        replacedSentence = ""        
        
        for word in sentenceWords:
            returnStr = self.searchRequired(word, root)
            #print word, returnStr
            if len(returnStr) > 0:
                replacedSentence += returnStr
                replacedSentence += " "
            else:
                replacedSentence += word
                replacedSentence += " "

        return replacedSentence[:-1]
        
        
        

