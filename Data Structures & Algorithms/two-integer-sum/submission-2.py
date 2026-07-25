class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_ = {}  # nums : index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in map_:
                return[map_[diff], i]
            map_[n] = i