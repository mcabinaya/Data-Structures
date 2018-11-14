class Solution(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        
    def isPalindrome(self, word):
        for i in range(0, len(word)):
            if word[i] != word[len(word)-1-i]:
                return False
        return True
        
    def insert(self, word, index):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i, w in enumerate(reversed(word)):
            #print i, w
            if w not in node:
                node[w] = {}
            if self.isPalindrome(word[0:len(word)-i]):
                if "isPalindrome" in node:
                    node["isPalindrome"].append(index)
                else:
                    node["isPalindrome"] = [index]
            node = node[w]
        node["wordIndex"] = index
        
    def searchPalindromes(self, word):
        output = []
        node = self.root
        while word:
            #if "wordIndex" in node:
            if ("wordIndex" in node) and (node["wordIndex"] >= 0):
                if self.isPalindrome(word):
                    output.append(node["wordIndex"])
            if word[0] not in node:
                return output
            node = node[word[0]]
            word = word[1:]
                
        if ("wordIndex" in node) and (node["wordIndex"] >= 0):
            output.append(node["wordIndex"])
        
        if "isPalindrome" in node:
            output.extend(node["isPalindrome"])
        return output
        
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        for i, word in enumerate(words):
            self.insert(word, i)
        
        result = []
        for i , word in enumerate(words):
            output = self.searchPalindromes(word)
            result.extend([[i, c] for c in output if i != c])
        return result
        
