import math
class Solution:
    # piles = [1,4,3,2], h = 9
    # k = 4 -> 2 -> 1
    # k = [1,max(piles)] -> [1, 4]
    # binary search valid k values
    # if median is valid search left, else search right
    # Time: O(nlog(m))
    # Space: O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calc_eating_hours(k: int) -> int: # Time: O(n)
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            return hours

        start, end = 1, max(piles)
        valid_k = 0
        while start <= end: # Time: O(logm) where m is max(piles)
            m = (start + end) // 2

            eating_hours = calc_eating_hours(m)
            if eating_hours <= h:
                valid_k = m
                end = m - 1
            else:
                start = m + 1
        
        return valid_k
