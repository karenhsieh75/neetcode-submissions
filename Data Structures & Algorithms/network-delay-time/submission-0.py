class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = {i:[] for i in range(n + 1)}
        for u, v, t in times:
            edges[u].append((v, t))
        
        minheap = [(0, k)]
        visited = set()
        time = 0

        while minheap:
            t1, u = heapq.heappop(minheap)
            if u in visited:
                continue
            visited.add(u)
            time = t1

            for v, t2 in edges[u]:
                if v not in visited:
                    heapq.heappush(minheap, (t1 + t2, v))

        if len(visited) == n:
            return time
        else:
            return -1