class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        else:
            result = strs[0]
            for i in range(len(result)):
                for j in range(1, len(strs)):
                    #print i,j
                    if i < len(strs[j]):
                        #print "first if"
                        if result[i] != strs[j][i]:
                            #print "second if -- break"
                            result = result[:i]
                            break
                    else:
                        #print "else -- break"
                        result = result[:i]
                        break
                if len(result) != len(strs[0]):
                    #print "outside break"
                    break

            return result
            
            
