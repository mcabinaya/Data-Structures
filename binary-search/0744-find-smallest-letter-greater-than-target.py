class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        #template 2
        #search for mid index greater than target where mid-1 is lesser than or equal to target
        left, right = 0, len(letters)
        while left < right:
            mid = (left + right) // 2
            compare_left = letters[mid-1] if (mid-1) >= 0 else float('-Inf')
            #print mid, compare_left
            if (compare_left <= target) & (letters[mid] > target) :
                return letters[mid]
            elif (compare_left <= target) & (letters[mid] <= target) :
                left = mid + 1
            else:
                right = mid

        if left < len(letters):
            compare_left = letters[(left-1)] if (left-1) >= 0 else float('-Inf')
            if (compare_left <= target) & (letters[left] > target) :
                    return letters[left]
        return letters[0]

        
