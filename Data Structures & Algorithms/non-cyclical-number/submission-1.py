class Solution:
    # Time: O(logn)
    # Space: O(logn)
    def isHappy(self, n: int) -> bool:
        visited = set()

        def sumOfSquares(n: int) -> int:
            temp = 0
            while n > 0:
                digit = n % 10
                temp += digit ** 2
                n //= 10
            return temp


        slow,fast = n, n
        while slow != 1 or fast != 1:
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))
            if slow != 1 and slow == fast:
                return False
        return True