class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest_count = 0
        count = 0
        for i in nums:
            if i==1:
                count += 1
            else:
                if count > largest_count:
                    largest_count = count
                count = 0
        if count > largest_count:
            return count
        else:
            return largest_count
            
