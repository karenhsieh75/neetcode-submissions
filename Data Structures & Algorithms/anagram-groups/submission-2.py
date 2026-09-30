class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map_ = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            map_[sorted_s].append(s)

        return list(map_.values())
        