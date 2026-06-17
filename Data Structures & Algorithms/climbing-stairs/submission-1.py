# 0
class Solution:
    # Time: O(2^n)
    # Space: O(n)
    # recurrence = f(0) = f(1) + f(2) = f(2) + f(3) + f(3) + f(4)
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def recurse(current: int) -> int:
            if current == n:
                return 1
            if current > n:
                return 0
            if cache[current] > -1:
                return cache[current]
            cache[current] = recurse(current + 1) + recurse(current + 2)
            return cache[current]
        return recurse(0)