class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = ""

        def dfs(cur, open_, close):
            if open_ + close == n * 2:
                res.append(cur)
                return
            
            if open_ == n:
                cur += ")"
                close += 1
                dfs(cur, open_, close)
                return
            
            if close == open_:
                cur += "("
                open_ += 1
                dfs(cur, open_, close)
                return   
            
            cur += "("
            open_ += 1
            dfs(cur, open_, close)

            cur = cur[:-1]
            open_ -= 1
            cur += ")"
            close += 1
            dfs(cur, open_, close)
        
        dfs(cur, 0, 0)
        return res
