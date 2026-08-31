class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {c:[] for c in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)

        visited = set()
        cycle = set()
        output = []
        def dfs(c):
            if c in visited:
                return True
            if c in cycle:
                return False
            
            cycle.add(c)
            for p in preMap[c]:
                if not dfs(p):
                    return False
            
            cycle.remove(c)
            visited.add(c)
            output.append(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return output
