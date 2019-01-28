class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        min_num = prices[0]
        max_diff = prices[1] - prices[0]
        
        for i in range(1, len(prices)):
            if (prices[i]-min_num) > max_diff:
                max_diff = prices[i]-min_num
                
            if prices[i] < min_num:
                min_num = prices[i]
                
        if max_diff < 0:
            return 0
        return max_diff
        
        