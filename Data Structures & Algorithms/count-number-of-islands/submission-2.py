class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        island = 0
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROW and 0 <= nc < COL and
                        grid[nr][nc] == "1" and (nr, nc) not in visited):
                        visited.add((nr, nc))  
                        q.append((nr, nc))        

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r, c) not in visited:
                    island += 1
                    visited.add((r, c))
                    bfs(r, c)
        
        return island
                    
                        
                        
