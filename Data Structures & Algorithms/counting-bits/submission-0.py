class Solution:
    def countBits(self, n: int) -> List[int]:
        def getOnes(x: int) -> int:
            count = 0
            while x > 0:
                if x & 1 == 1:
                    count += 1
                x >>= 1
            return count
        
        return [getOnes(i) for i in range(n+1)]