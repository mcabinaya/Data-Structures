class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Divide-and-Conquer Solution
        def reverseStringUtils(start, end, s):
            if start >= end:
                return
            s[start], s[end] = s[end], s[start]
            return reverseStringUtils(start+1, end-1, s)
        
        reverseStringUtils(0, len(s)-1, s)
