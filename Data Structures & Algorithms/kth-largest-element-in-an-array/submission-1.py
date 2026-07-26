class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heap = heapq.heapify(nums)

        res = 0
        for _ in range(k):
            res = -1 * heapq.heappop(nums)
        
        return res
        