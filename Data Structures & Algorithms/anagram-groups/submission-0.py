class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map_ = {}  # sorted str : [index]
        result = []

        for i, s in enumerate(strs):

            s_ = ''.join(sorted(s))
            if s_ in map_:
                map_[s_].append(i)
            else:
                map_[s_] = [i]
        
        for s in map_:
            group = [strs[i] for i in map_[s]]
            result.append(group)
        
        return result
            

        '''
        "act" : [0, 3]
        "opts" : [1, 2, 4] 
        "aht" : [5]
        '''