class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return [[]]
        elif len(nums)==1:
            return [[],[nums[0]]]
        num = nums[0]
        returned = self.subsets(nums[1:])
        temp = []
        for l in returned:
            temp.append(l+[num])
        return temp+returned
