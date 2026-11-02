class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        
        for n in nums:
            cur = max(prev1 + n, prev2)
            prev1 = prev2
            prev2 = cur
        
        return prev2
