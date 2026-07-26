class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        max_heap = [-c for c in count.values()]
        heapq.heapify(max_heap)
        q = deque()

        time = 0
        while max_heap or q:
            time += 1

            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1  # since we use negative values
                if count:
                    q.append([count, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time

        