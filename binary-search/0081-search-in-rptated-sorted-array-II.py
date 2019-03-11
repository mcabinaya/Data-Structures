class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        def binarySearch(nums, left, right, target):
            mid = (left+right)/2
            if nums[mid] == target: #base case
                return True
            if right < left: #base case
                return False
            
            if nums[left] < nums[mid]: #left array is normally sorted
                if ((nums[left] <= target) and (target < nums[mid])):
                    return binarySearch(nums, left, mid-1, target)
                else:
                    return binarySearch(nums, mid+1, right, target)
            
            elif nums[mid] < nums[right]: #right array is normally sorted
                if ((nums[mid] < target) and (target <= nums[right])):
                    return binarySearch(nums, mid+1, right, target)
                else:
                    return binarySearch(nums, left, mid-1, target)
            
            elif ((nums[left] == nums[mid]) or (nums[mid] == nums[right])): #left or right arrays  are same
                if ((nums[left] == nums[mid]) and (nums[mid] != nums[right])): #left array is same
                    return binarySearch(nums, mid+1, right, target)
                elif ((nums[left] != nums[mid]) and (nums[mid] == nums[right])): #right array is same
                    return binarySearch(nums, left, mid-1, target)
                else:
                    result = binarySearch(nums, left, mid-1, target)
                    if (result != True):
                        return binarySearch(nums, mid+1, right, target)
                    else:
                        return result
        
        # Solution
        if len(nums) > 0:
            return binarySearch(nums, 0, len(nums)-1, target)
        return False
        
