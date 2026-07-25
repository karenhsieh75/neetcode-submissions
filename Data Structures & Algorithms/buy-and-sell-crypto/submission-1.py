class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        accuProfit = 0
        maxProfit = 0

        for i in range(len(prices) - 1):
            diff = prices[i + 1] - prices[i]
            accuProfit += diff
            if accuProfit > 0:
                maxProfit = max(maxProfit, accuProfit)
            else:
                accuProfit = 0
        
        return maxProfit