class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pivot_index = -1
        tot_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = tot_sum - left_sum - nums[i]
            if left_sum == right_sum:
                pivot_index = i
                break
            left_sum = left_sum + nums[i]
        return pivot_index
                
                
        
