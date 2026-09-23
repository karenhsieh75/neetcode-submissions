class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])

        result_matrix = [[float("inf")] * COL for _ in range(ROW)]

        def dfs(r, c, prev):
            if r < 0 or r >= ROW or c < 0 or c >= COL or matrix[r][c] <= prev:
                return 0
            if result_matrix[r][c] != float("inf"):
                return result_matrix[r][c]
            
            result_matrix[r][c] = 1 + (max(dfs(r + 1, c, matrix[r][c]),
                                     dfs(r - 1, c, matrix[r][c]),
                                     dfs(r, c + 1, matrix[r][c]),
                                     dfs(r, c - 1, matrix[r][c])))
            
            return result_matrix[r][c]
            
        
        res = 0
        for r in range(ROW):
            for c in range(COL):
                res = max(res, dfs(r, c, -1))

        return res