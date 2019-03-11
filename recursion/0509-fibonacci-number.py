class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        #using recursion with memoization
        def fibUtils(N, cache):
            if (N == 0) or (N == 1):
                return N
            if N in cache:
                return cache[N]
            result = fibUtils(N-1, cache) + fibUtils(N-2, cache)
            cache[N] = result
            return result
        
        cache = {}
        return fibUtils(N, cache)   
