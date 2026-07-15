class Solution:
    # Time: O(n)
    # Space: O(1)
    # def myPow(self, x: float, n: int) -> float:
    #     abs_n = abs(n)
    #     res = 1
    #     for _ in range(abs_n):
    #         res *= x
    #     if n < 0:
    #         res = 1 / res
    #     return res

    # Time: O(logn)
    # Space: O(logn)
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if abs(n) == 1:
            return x if n > 0 else 1 / x
        res = self.myPow(x, n//2) * self.myPow(x, n//2)
        return res * x if n % 2 == 1 else res
        
