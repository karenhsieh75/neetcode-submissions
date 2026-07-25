class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        s1_count = {}
        for s in s1:
            s1_count[s] = 1 + s1_count.get(s, 0)
        target_count = s1_count.copy()

        for l in range(len(s2) - len(s1) + 1):

            if s2[l] not in s1_count:
                continue
            
            for r in range(l, l + len(s1)):
                target_count[s2[r]] = target_count.get(s2[r], 0) - 1
            
            if set(target_count.values()) == {0}:
                return True
            else:
                target_count = s1_count.copy()
        
        return False
                