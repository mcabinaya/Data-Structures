class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x==1:
            return x
        else:
            l = 1
            r = x
            while l <= r:
                m = (l + r) // 2
                print l, r, m
                if m*m == x:
                    return m
                elif m*m < x:
                    #print "less"
                    l = m+1
                else:
                    #print "great"
                    r = m-1

            return m-1 if m*m > x else m

