class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # [[d1, [x1, y1]], [d2, [x1, y1]]]
        min_heap = [[math.sqrt(x ** 2 + y ** 2), [x, y]] for x, y in points]
        heapq.heapify(min_heap)
        res = []

        for i in range(k):
            point = heapq.heappop(min_heap)[1]
            res.append(point)
        
        return res