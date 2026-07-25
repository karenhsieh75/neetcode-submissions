class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        nums_with_index = [[i, n] for i, n in enumerate(nums)]
        return self.binary_search(nums_with_index, target)
        
        
    def binary_search(self, nums: List[[int, int]], target: int) -> int:

        if len(nums) == 1:
            return nums[0][0] if nums[0][1] == target else -1
        else:
            m = len(nums) // 2
            if nums[m][1] > target:
                return self.binary_search(nums[0:m], target)
            elif nums[m][1] < target:
                return self.binary_search(nums[m:len(nums)], target)
            else:
                return nums[m][0]