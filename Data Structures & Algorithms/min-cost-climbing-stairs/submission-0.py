class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one, two = cost[-2], cost[-1]

        for i in range(n - 3, -1, -1):
            temp = one
            one = min(one, two) + cost[i]
            two = temp
        
        return min(one, two)
        