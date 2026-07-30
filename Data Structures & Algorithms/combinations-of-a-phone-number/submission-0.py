class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        char_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def dfs(i):
            nonlocal res

            if i == len(digits):
                return

            if i == 0:
                res = char_map[digits[i]].copy()
                dfs(i + 1)
                return
            
            cur = []
            for s in res:
                for c in char_map[digits[i]]:
                    new_s = s + c
                    cur.append(new_s)
            res = cur.copy()
            dfs(i + 1)
        
        dfs(0)
        return res

                        