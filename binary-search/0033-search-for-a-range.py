class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.searchFirst(nums, target), self.searchLast(nums, target)]
        
    
    def searchFirst(self, nums, target):
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) // 2
            extra_check = nums[mid-1] if mid-1 >= 0 else float('-Inf')
            if (extra_check < target) & (nums[mid] == target):
                return mid
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid
            else:
                right = mid
        
        if left == right:
            extra_check = nums[left-1] if left-1 >= 0 else float('-Inf')
            if (extra_check < target) & (nums[left] == target): return left
        return -1
    
    def searchLast(self, nums, target):
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) // 2
            extra_check = nums[mid+1] if mid+1 < len(nums) else float('Inf')
            if (nums[mid] == target) & (extra_check > target):
                return mid
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid
            else:
                left = mid+1
                
        if left == right:
            extra_check = nums[right+1] if right+1 < len(nums) else float('Inf')
            if (nums[right] == target) & (extra_check > target): return right
        return -1
