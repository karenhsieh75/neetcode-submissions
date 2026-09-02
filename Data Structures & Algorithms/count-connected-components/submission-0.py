class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors = {i:[] for i in range(n)}
        for x, y in edges:
            neighbors[x].append(y)
            neighbors[y].append(x)

        visited = set()

        def dfs(i):
            if i in visited:
                return 
            
            visited.add(i)
            for n in neighbors[i]:
                dfs(n)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count

        