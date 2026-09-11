class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
            minUsed = [amount + 1] * (amount + 1)  # minUsed[n] store the mininum coins used to add to n
            minUsed[0] = 0

            for a in range(1, amount + 1):
                for c in coins:
                    if a - c >= 0:
                        minUsed[a] = min(minUsed[a], 1 + minUsed[a - c])

            if minUsed[amount] == amount + 1:
                return -1
            else:
                return minUsed[amount] 

