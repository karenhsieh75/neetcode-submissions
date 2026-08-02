class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROW, COL = len(grid), len(grid[0])
        max_area = 0
        visited = set()

        def bfs(r, c) -> int:  # return the area of current island
            area = 0
            q = deque()
            q.append((r, c))
            
            while q:
                area += 1
                r, c = q.popleft()

                for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROW and 0 <= nc < COL 
                    and grid[nr][nc] == 1 and (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))
            
            return area

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r, c) not in visited:
                    visited.add((r, c))
                    max_area = max(max_area, bfs(r, c))
        
        return max_area
        