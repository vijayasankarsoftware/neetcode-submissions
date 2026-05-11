class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0

        bought_price = prices[0]

        for next_day_price in prices[1:]:
            if bought_price > next_day_price:
                bought_price = next_day_price
            profit = max(profit, next_day_price - bought_price)

        return profit