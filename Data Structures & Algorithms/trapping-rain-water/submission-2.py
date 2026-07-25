class Solution:
    def trap(self, height: List[int]) -> int:
        # trap at loc i = min(max_l, max_r) - height[i]

        l, r = 0, len(height) - 1
        water = 0
        max_l = height[l]
        max_r = height[r]

        while l < r:
            if max_l <= max_r:
                l += 1
                max_l = max(max_l, height[l])
                water += max(max_l - height[l], 0)
            else:
                r -= 1
                max_r = max(max_r, height[r])
                water += max(max_r - height[r], 0)
        
        return water


