class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        def dfs(open_, close):
            if open_ + close == n * 2:
                res.append("".join(cur))
                return
            
            if open_ < n:
                cur.append("(")
                dfs(open_ + 1, close)
                cur.pop()
            
            if close < open_:
                cur.append(")")
                dfs(open_, close + 1)
                cur.pop()
            
        dfs(0, 0)
        return res
