class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            # prereq 修完後，可以解鎖 course
            graph[prereq].append(course)
            # course 多了一個 prerequisite
            # TODO
            indegree[course] += 1

        queue = deque()

        # 把所有 indegree 為 0 的課放入 queue
        # TODO
        for c in range(numCourses):
            if indegree[c] == 0:
                queue.append(c)

        completed = 0

        while queue:
            course = queue.popleft()
            completed += 1

            # 更新被這門課解鎖的課程
            # TODO
            for c in graph[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    queue.append(c)

        return completed == numCourses