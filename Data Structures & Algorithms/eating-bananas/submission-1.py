class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # possible speed k = [1, 2, 3, ..., max(piles)]
        # implement binary search on this range

        l, r = 1, max(piles)
        min_k = r  # initialize min k with the largest possible k

        while l <= r:
            k = (l + r) // 2
            hours = sum([math.ceil(p / k) for p in piles])

            if hours > h:
                l = k + 1
            else:
                min_k = min(min_k, k)
                r = k - 1

        return min_k
                
        

        