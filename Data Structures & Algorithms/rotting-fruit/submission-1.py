class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        q = deque()

        # find rotten fruits and fresh fruits
        fresh = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr < 0 or nr >= ROW or nc < 0 or nc >= COL or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
            
            minutes += 1

        if fresh == 0:
            return minutes
        else:
            return -1


                