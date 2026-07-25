class Solution:
    def findMin(self, nums: List[int]) -> int:

        # two ideas for this question
        # 1. nums[m] >= nums[l] means m is in the left portion => search right
        # 2. if nums[l] < nums[r], directly return nums[l]
        
        l, r = 0, len(nums) - 1
        min_val = 2000

        while l <= r:
            m = (l + r) // 2
            min_val = min(min_val, nums[m])
            if nums[l] <= nums[r]:
                min_val = min(min_val, nums[l])
                break
            elif nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return min_val

