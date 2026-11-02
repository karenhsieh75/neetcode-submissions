class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        neighbors = defaultdict(list)
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)

        visited = set()
        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)
            for n in neighbors[i]:
                dfs(n)

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        
        return res