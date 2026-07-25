class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_ = set(nums)
        if len(set_) < len(nums):
            return True
        else:
            return False