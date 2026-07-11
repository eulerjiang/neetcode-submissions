class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        
        lower = float('inf')

        for price in prices:
            if price < lower:
                lower = price
            else:
                max_profit = max(max_profit, price - lower)

        return max_profit


