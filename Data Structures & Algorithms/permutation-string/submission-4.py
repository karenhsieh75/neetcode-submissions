class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Version 3 -- with extra variable "matches"
        # See previous submissions for more
        
        if len(s1) > len(s2):
            return False
        
        s1_count = {}
        for s in s1:
            s1_count[s] = s1_count.get(s, 0) + 1
        
        window_count = {}
        for i in range(len(s1)):
            window_count[s2[i]] = window_count.get(s2[i], 0) + 1

        # initialize matches
        matches = 0
        for char, count in s1_count.items():
            if window_count.get(char, 0) == count:
                matches += 1

        if matches == len(set(s1)):
            return True

        # sliding window
        l = 0
        for r in range(len(s1), len(s2)):

            # add tail
            window_count[s2[r]] = window_count.get(s2[r], 0) + 1

            if s2[r] in s1_count and window_count[s2[r]] == s1_count[s2[r]]:
                matches += 1
            elif s2[r] in s1_count and window_count[s2[r]] == s1_count[s2[r]] + 1:
                matches -= 1

            # remove head
            window_count[s2[l]] = window_count.get(s2[l], 0) - 1

            if s2[l] in s1_count and window_count[s2[l]] == s1_count[s2[l]]:
                matches += 1
            elif s2[l] in s1_count and window_count[s2[l]] == s1_count[s2[l]] - 1:
                matches -= 1

            if matches == len(set(s1)):
                return True

            l += 1
        
        return False
        




                