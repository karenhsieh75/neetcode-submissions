class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        neighbors = {i:[] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]

                dist = abs(x1 - x2) + abs(y1 - y2)
                neighbors[i].append((dist, j))
                neighbors[j].append((dist, i))
        
        minheap = [(0, 0)]
        visited = set()
        cost = 0
        while len(visited) != n:
            d1, n1 = heapq.heappop(minheap)
            if n1 not in visited:
                for d2, n2 in neighbors[n1]:
                    heapq.heappush(minheap, (d2, n2)) 
                visited.add(n1)
                cost += d1
        
        return cost


        