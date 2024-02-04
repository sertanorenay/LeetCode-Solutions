class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for buy_index in range(len(prices)):
            for sell in prices[buy_index:]:
                if sell - prices[buy_index] > max_profit:
                    max_profit = sell - prices[buy_index]
        return max_profit
    """
    TIME LIMIT
    """