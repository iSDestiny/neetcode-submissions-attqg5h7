class Solution:
    def myPow(self, x: float, n: int) -> float:
        abs_n = abs(n)
        res = 1
        for _ in range(abs_n):
            res *= x
        if n < 0:
            res = 1 / res
        return res
