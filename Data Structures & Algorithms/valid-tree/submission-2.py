class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbors = {i:[] for i in range(n)}
        for x, y in edges:
            neighbors[x].append(y)
            neighbors[y].append(x)
        
        visited = set()
        def dfs(cur, prev):
            if cur in visited:
                return False 
            
            visited.add(cur)
            for n in neighbors[cur]:
                if n == prev:
                    continue
                if not dfs(n, cur):
                    return False
            
            return True
        
        if dfs(0, -1) and len(visited) == n:
            return True
        else:
            return False
        
        