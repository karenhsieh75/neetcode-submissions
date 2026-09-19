class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # key: (i, buying), value: max profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                action = dfs(i + 1, not buying) - prices[i]
            else:
                action = dfs(i + 2, not buying) + prices[i]

            cooldown = dfs(i + 1, buying)
            maxP = max(action, cooldown)
            dp[(i, buying)] = maxP

            return maxP
        
        return dfs(0, True)
        