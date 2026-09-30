class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map_ = {}  # num : index

        for i, n in enumerate(nums):
            if target - n in map_:
                return [map_[target - n], i]
            else:
                map_[n] = i