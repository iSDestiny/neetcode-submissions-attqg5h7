class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            if n & (2**i) == (2**i):
                count += 1
        return count