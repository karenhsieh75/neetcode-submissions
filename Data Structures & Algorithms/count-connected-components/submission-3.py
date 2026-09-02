class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def findPar(i):
            p = i
            while p != par[p]:
                p = par[p]
            return p
        
        def union(a, b):
            pa = findPar(a)
            pb = findPar(b)

            if pa == pb:
                return 0
            
            if rank[pa] >= rank[pb]:
                par[pb] = pa
                rank[pa] += rank[pb]
            else:
                par[pa] = pb
                rank[pb] += rank[pa]
            
            return 1
        
        groups = n
        for a, b in edges:
            groups -= union(a, b)
        
        return groups
            

        

        