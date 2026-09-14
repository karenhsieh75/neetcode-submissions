class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if (total % 2) != 0:
            return False

        target = total // 2
        curSet = set()
        curSet.add(nums[-1])

        for i in range(len(nums) - 2, -1, -1):
            nextSet = curSet.copy()
            for n in curSet:
                nextSet.add(n + nums[i])
            curSet = nextSet 
        
        if target in curSet:
            return True
        else:
            return False

        