class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        subtracted_dict = {}
        
        for i in range(0, len(nums)):
            if nums[i] in subtracted_dict:
                return [subtracted_dict[nums[i]], i]
            else:
                subtracted_dict[target-nums[i]] = i
        
        
