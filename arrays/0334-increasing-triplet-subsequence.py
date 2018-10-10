class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # keep track of continuous first and second
        first = float('inf')
        second = float('inf')
        
        for i in nums:
            if i <= first:
                first = i
            elif i<=second: 
                second = i
            else: #if you find one number greater than first and second return True
                return True
        return False
                

