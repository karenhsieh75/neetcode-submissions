class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums) - 1):
            prefix *= nums[i]
            result[i + 1] *= prefix
        
        postfix = 1
        for i in range(len(nums) - 1, 0, -1):
            postfix *= nums[i]
            result[i - 1] *= postfix
        
        return result