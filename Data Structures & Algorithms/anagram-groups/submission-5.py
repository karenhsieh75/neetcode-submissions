class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map_ = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            count = tuple(count)
            if count in map_:
                map_[count].append(s)
            else:
                map_[count] = [s]
        
        return list(map_.values())
            
                
        