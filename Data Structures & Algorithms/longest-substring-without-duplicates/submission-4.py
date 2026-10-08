class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        l = 0
        window = set()
        max_len = 1

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1

            window.add(s[r])
            max_len = max(max_len, len(window))
        
        return max_len
            