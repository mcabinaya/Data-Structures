class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] >= nums[right]:
                left = mid+1
            else:
                right = mid
        return nums[mid]      
            
