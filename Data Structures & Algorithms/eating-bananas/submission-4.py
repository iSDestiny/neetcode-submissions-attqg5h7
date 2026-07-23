import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat_all(k: int) -> bool:
            hour = 0
            for b in piles:
                hour += math.ceil(b/k)
            return hour <= h
        
        l,r = 1, max(piles)
        lowest = max(piles)
        while l <= r:
            mid = (l+r) // 2
            if eat_all(mid):
                lowest = min(lowest, mid)
                r = mid - 1
            else:
                l = mid + 1
        return lowest
