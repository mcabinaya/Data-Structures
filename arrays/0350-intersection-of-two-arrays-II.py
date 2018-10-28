class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
                    
        mydict = {}
        for n in nums1: #O(n) add values in nums1 to dict
            if n not in mydict:
                mydict[n] = 1
            else:
                mydict[n] += 1
        
        result = []
        for n in nums2:
            if n in mydict: #check in mydict if its present
                result.append(n)
                mydict[n] -= 1
                if mydict[n] == 0:
                    mydict.pop(n)
        return result
                
