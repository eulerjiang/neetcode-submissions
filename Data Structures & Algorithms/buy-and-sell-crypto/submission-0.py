class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        i , j = 0, 0

        if len(prices) <= 1:
            return 0

        while i < len(prices) - 1:
            j = i + 1
            while j < len(prices):
                if prices[j] - prices[i] > maxProfit:
                    maxProfit = prices[j] - prices[i]
                j += 1
            i += 1
        return maxProfit