class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        
        # recursively divide until n becomes 0
        temp = self.myPow(x, int(float(n)/2))
        
        
        if (n%2 == 0):
            return temp*temp
        else:
            if n > 0:
                return x*temp*temp
            else:
                return (temp * temp) / x
