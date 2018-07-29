class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=len(numbers)-1
        while i < j:
            temp_sum = numbers[i] + numbers[j]
            if temp_sum == target:
                break
            elif temp_sum < target:
                i+=1
            else:
                j-=1
        return [i+1, j+1]
    
