class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0 or num==1:
            return True
        else:
            # binary search for the square root close to 'num'
            l = 1
            r = num
            while l <= r:
                m = (l + r) // 2
                #print l, r, m
                if m*m == num:
                    return True
                elif m*m < num:
                    l = m+1
                else:
                    r = m-1
            # loop ends with the closest square root number, check if its a perfect square
            return True if m*m == num else False

