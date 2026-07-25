class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_set = set()
        max_len = 0
        # l, r = 0, 0
        l = 0

        for r in range(len(s)):
        # while r < len(s):
            while s[r] in window_set:
                window_set.remove(s[l])
                l += 1
            
            window_set.add(s[r])
            max_len = max(max_len, r - l + 1)
            # r += 1
        
        return max_len