# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n+1
        while left < right:
            mid = (left+right) // 2
            print left, right, mid
            mid_bad = isBadVersion(mid)
            mid_before_bad = isBadVersion(mid-1)
            if (mid_bad == True) & (mid_before_bad == False):
                return mid
            elif (mid_bad == False) & (mid_before_bad == False):
                left = mid+1
            else:
                right = mid
        
        if (left != n+1) and (isBadVersion(left) == True) and (isBadVersion(left-1) == False):
            return left
        return -1

                
            
        
