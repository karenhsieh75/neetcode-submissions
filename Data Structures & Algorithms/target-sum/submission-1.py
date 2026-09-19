class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        
        def dfs(i, curSum): # return the num of ways
            if i == len(nums):
                return 1 if curSum == target else 0
            if (i, curSum) in cache:
                return cache[(i, curSum)]
            
            cache[(i, curSum)] = dfs(i + 1, curSum + nums[i]) + dfs(i + 1, curSum - nums[i])

            return cache[(i, curSum)]
        
        return dfs(0, 0)
