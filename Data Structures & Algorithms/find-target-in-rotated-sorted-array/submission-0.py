class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 左半部分 => 比我大一定往右
        # 比我小且比 nums[l] 小 => 往右
        # 比我小且比 nums[l] 大 => 往左

        # 右半部分 => 比我小一定往左
        # 比我大且比 nums[l] 小 => 往右
        # 比我大且比 nums[l] 大 => 往左

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:  # left portion
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1

            else:  # right portion
                if target > nums[m] and target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1

