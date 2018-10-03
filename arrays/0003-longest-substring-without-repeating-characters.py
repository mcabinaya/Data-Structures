class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        tempLen = 0
        visited = []
        for i in range(len(s)):
            #char not visited
            if s[i] not in visited:
                visited.append(s[i])
                tempLen += 1
            #char visited - initialize visited again and set maxLen
            else:
                findIndex = visited.index(s[i])
                if tempLen > maxLen:
                    maxLen = tempLen
                visited = visited[findIndex+1:]
                tempLen = tempLen - findIndex
                visited.append(s[i])
        if tempLen > maxLen:
            return tempLen
        return maxLen
        
