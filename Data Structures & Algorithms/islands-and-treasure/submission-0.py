class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def addCell(r, c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or (r, c) in visited or grid[r][c] == -1:
                return

            q.append((r, c))
            visited.add((r, c))
                

        # add treasure to queue
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        dist = 0
        while q:

            for i in range(len(q)):  # current layer
                r, c = q.popleft()
                grid[r][c] = dist
                
                addCell(r - 1, c)
                addCell(r + 1, c)
                addCell(r, c - 1)
                addCell(r, c + 1)
            
            dist += 1
