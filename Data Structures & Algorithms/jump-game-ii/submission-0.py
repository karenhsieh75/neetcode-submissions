class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            move = 0
            for i in range(l, r + 1):
                move = max(move, i + nums[i])
            l = r + 1
            r = move
            res += 1
    
        return res
        