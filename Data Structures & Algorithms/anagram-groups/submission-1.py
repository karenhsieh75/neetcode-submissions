class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map_ = {}  # counter : [str]

        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord("a")] += 1
            
            counter = tuple(counter)
            if counter in map_:
                map_[counter].append(s)
            else:
                map_[counter] = [s]
        
        return list(map_.values())
