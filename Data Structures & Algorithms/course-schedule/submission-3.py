class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        unlockMap = defaultdict(list)
        indegree = [0] * numCourses  # indegree [i]: how many pre left for course i
        for c, p in prerequisites:
            unlockMap[p].append(c)
            indegree[c] += 1

        queue = deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                queue.append(c)

        completed = 0
        while queue:
            p = queue.popleft()
            completed += 1

            for c in unlockMap[p]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    queue.append(c)
        
        return completed == numCourses

            