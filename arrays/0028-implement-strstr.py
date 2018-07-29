class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        len_haystack = len(haystack)
        len_needle = len(needle)
        if len_needle == 0:
            return 0
        elif len_needle > len_haystack:
            return -1
        else:
            start_index = -1
            count = 0
            i = 0
            while i < len_haystack:
                #print "--- ",i, start_index, count
                if (haystack[i] == needle[count]):
                    if (start_index == -1):
                        start_index = i
                        count += 1
                        #print "1st loop: ", start_index, count
                    else:
                        #print "2nd loop: ", start_index, count
                        count += 1
                    if count == len_needle:
                        #print "breaking"
                        break
                    else:
                        i += 1
                        continue
                if (haystack[i] != needle[count]) and (start_index != -1):
                    i = start_index+1
                    start_index = -1
                    count = 0
                    #print "3rd loop: ", start_index, count
                    continue
                i += 1
            if (start_index != -1) and (count != len_needle):
                start_index = -1
            return start_index
            
