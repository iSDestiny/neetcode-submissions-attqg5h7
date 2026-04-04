from math import ceil

class Solution:
    # piles = [1,4,3,2], h = 9
    # l = 1, r = 4
    # mid = 2
    # midTime = 6
    # minK = 2
    # l = 1, r = 1
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minK = max(piles)

        while l <= r:
            mid = (l + r) // 2
            midTime = self.getTotalEatingTime(piles, mid)

            if midTime <= h:
                minK = mid
                r = mid - 1
            else:
                l = mid + 1

        return minK 
    

    # Time: O(n)
    def getTotalEatingTime(self, piles: List[int], eatingRate: int) -> int:
        totalTime = 0
        for p in piles:
            totalTime += int(ceil(float(p) / eatingRate))
        return totalTime