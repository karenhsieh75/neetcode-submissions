class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = { i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)

        visited = set()
        def dfs(i):  # return whether course i can be finished
            if i in visited:
                return False
            elif preMap[i] == []:
                return True
            
            visited.add(i)
            for c in preMap[i]:
                if not dfs(c):
                    return False
            
            preMap[i] = []
            visited.remove(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True



        
        