class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            compare_left = nums[mid-1] if (mid-1) >= 0 else float('-Inf')
            compare_right = nums[mid+1] if (mid+1) < len(nums) else float('-Inf')
            print nums[mid], compare_left, compare_right
            if nums[mid] < compare_left:
                right = mid
            elif nums[mid] < compare_right:
                left = mid+1
            else:
                return mid
        return mid
            
