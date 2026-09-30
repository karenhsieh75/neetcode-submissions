class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map_ = {}

        for s in strs:
            sorted_s = "".join(sorted(s))

            if sorted_s in map_:
                map_[sorted_s].append(s)
            else:
                map_[sorted_s] = [s]

        return list(map_.values())
        