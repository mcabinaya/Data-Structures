class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        
        elif len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        else:
            for i in range(0, len(nums)-1):
                if nums[i] > nums[i+1]:
                    break

            arr1 = nums[:i+1]
            arr2 = nums[i+1:]
            #print i
            #print arr1
            #print arr2

            index1 = self.binarySearch(arr1, target)
            index2 = self.binarySearch(arr2, target)
            #print index1
            #print index2

            if (index1 != -1) & (index2 == -1):
                return index1
            elif (index1 == -1) & (index2 != -1):
                return i+index2+1
            else:
                return -1      
        
    def binarySearch(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l + r ) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        return -1
    
