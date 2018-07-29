class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = 0
        init_len = len(nums)
        while i < len(nums):
            if nums[i] == val:
                j += 1
                del nums[i]
            else:
                i += 1
        return init_len-j
        
            
        
