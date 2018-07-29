# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n
        while l <= r:
            m = (l+r)//2
            #print l, r, m
            guessed = guess(m)
            if guessed == 0:
                return m
            elif guessed == 1:
                l = m+1
            else:
                r = m-1
        
            
