class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        first, second = 0, 1
        nums[1] = max(nums[0], nums[1])
        
        for n in range(2, len(nums)):
            nums[n] = max(nums[first] + nums[n], nums[second])
            first += 1
            second += 1
        
        return nums[len(nums) - 1]
