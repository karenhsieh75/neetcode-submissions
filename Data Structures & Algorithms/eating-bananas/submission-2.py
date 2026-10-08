class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_k = r

        while l <= r:
            k = (l + r) // 2
            hours = sum([math.ceil(p / k) for p in piles])
            if hours <= h:
                min_k = k
                r = k - 1
            else:
                l = k + 1
        
        return min_k
