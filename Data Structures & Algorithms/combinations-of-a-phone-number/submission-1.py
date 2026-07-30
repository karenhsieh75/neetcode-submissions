class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        res = [""]
        char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        for d in digits:
            cur = []
            for s in res:
                for c in char_map[d]:
                    new_s = s + c
                    cur.append(new_s)
            res = cur

        return res

                        