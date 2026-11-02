class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        heap = []
        heapq.heapify(heap)

        for key, value in freq.items():
            heapq.heappush(heap, (value, key))

        while len(heap) > k:
            heapq.heappop(heap)
        
        res = []
        for value, key in heap:
            res.append(key)
        
        return res
        
        
        