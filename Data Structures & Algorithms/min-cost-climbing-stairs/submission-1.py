# [1,2,3]
#    2 -> X
#    2->5->X
#  1 -> 4 -> x
#  1->3->X
#  1->3->6->X
class Solution:
    # Time: O(2^n)
    # Space: O(n)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        oneCache = [-1] * n
        def recurse(idx) -> int:
            if idx >= n:
                return 0
            if oneCache[idx] != -1:
                return oneCache[idx]
            oneCache[idx] = cost[idx] + min(recurse(idx+1), recurse(idx+2))
            return oneCache[idx]
        return min(recurse(0), recurse(1))