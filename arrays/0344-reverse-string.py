class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s) - 1
        result = list(s)
        #print result
        while i < j:
            result[i] = s[j]
            result[j] = s[i]          
            i += 1
            j -= 1
        #print result
        #print str(result)
        return ''.join(result)
        
