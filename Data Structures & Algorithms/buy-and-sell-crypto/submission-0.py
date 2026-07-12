class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = float('inf')
        max_diff = 0

        for price in prices:
            if price < lowest_price:
                lowest_price = price
            elif price - lowest_price > max_diff:
                max_diff = price - lowest_price
        return max_diff