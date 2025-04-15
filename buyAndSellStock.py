from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> List[int]:
        if prices is None:
            return

        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            minPrice = min(price, minPrice)
            maxProfit = max(maxProfit, price - minPrice)

        return maxProfit

sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4])) # Output: 5 (Buy at 1, sell at 6)