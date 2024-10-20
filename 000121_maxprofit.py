class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l, r = r, r + 1
                continue
            if profit > maxProfit:
                maxProfit = profit
            r += 1

        return maxProfit
