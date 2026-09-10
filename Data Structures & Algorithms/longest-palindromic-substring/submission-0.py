class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        res = ""

        for i in range(len(s)):

            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curLen = r - l + 1
                if curLen > longest:
                    longest = curLen
                    res = s[l:r+1]
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curLen = r - l + 1
                if curLen > longest:
                    longest = curLen
                    res = s[l:r+1]
                l -= 1
                r += 1
        
        return res
        
    
        