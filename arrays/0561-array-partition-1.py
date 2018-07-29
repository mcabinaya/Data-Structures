class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_num = sorted(nums)
        result = 0
        for i in range(0, len(sorted_num), 2):
            result += min(sorted_num[i], sorted_num[i+1])
        return result
