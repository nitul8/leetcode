# Best time to buy and sell stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = float('inf')
        max_profit = 0

        for i in prices:
            if i < min_price:
                min_price = i
            if i - min_price > max_profit:
                max_profit = i - min_price
        return max_profit