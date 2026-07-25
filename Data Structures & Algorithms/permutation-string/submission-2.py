class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        s1_count = {}
        for s in s1:
            s1_count[s] = s1_count.get(s, 0) + 1
        
        window_count = {}
        for i in range(len(s1)):
            window_count[s2[i]] = window_count.get(s2[i], 0) + 1

        if window_count == s1_count:
            return True

        l = 0
        for r in range(len(s1), len(s2)):

            # add tail
            window_count[s2[r]] = window_count.get(s2[r], 0) + 1

            # remove head
            window_count[s2[l]] = window_count.get(s2[l], 0) - 1
            if window_count[s2[l]] == 0:
                del window_count[s2[l]]
            
            if window_count == s1_count:
                return True
            l += 1
        
        return False
        




                