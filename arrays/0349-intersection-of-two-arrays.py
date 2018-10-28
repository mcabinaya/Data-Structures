class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        i = 0
        j = 0
        
        nums1.sort()
        nums2.sort()
        
        #using two pointers
        result = []
        while (i< len(nums1)) & (j < len(nums2)):
            if nums1[i] == nums2[j]:
                if nums1[i] not in result:
                    result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result
                
                
          
