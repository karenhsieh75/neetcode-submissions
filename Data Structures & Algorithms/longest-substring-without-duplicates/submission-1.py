class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_set = set()
        max_len = 0
        l, r = 0, 0

        while r < len(s):
            while s[r] in window_set:
                window_set.remove(s[l])
                l += 1
            
            window_set.add(s[r])
            cur_len = r - l + 1
            max_len = max(max_len, cur_len)
            r += 1
        
        return max_len