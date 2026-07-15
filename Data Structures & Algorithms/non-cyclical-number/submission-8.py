class Solution:
    # Time: O(logn)
    # Space: O(1)
    def isHappy(self, n: int) -> bool:
        visited = set()

        def sumOfSquares(n: int) -> int:
            temp = 0
            while n > 0:
                digit = n % 10
                temp += digit ** 2
                n //= 10
            return temp


        slow,fast = n, sumOfSquares(n)
        while slow != fast:
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))
        return True if fast == 1 else False