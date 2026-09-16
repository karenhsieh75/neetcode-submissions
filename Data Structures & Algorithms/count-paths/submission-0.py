class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        l = max(m - 1, n - 1) # large
        s = min(m - 1, n - 1) # small

        res = 1
        for num in range(l + 1, l + s + 1):
            res *= num
        
        for num in range(1, s + 1):
            res /= num
        
        return int(res)
        