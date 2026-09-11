class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        cache = {}

        def dfs(i):
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            if i in cache:
                return cache[i]

            # now the first digit is valid
            res = dfs(i + 1)

            # check if taking two digits is also valid
            if i + 1 < n and int(s[i:i + 2]) <= 26:
                res += dfs(i + 2)
            
            cache[i] = res
            return res
        
        return dfs(0)
            
            

            