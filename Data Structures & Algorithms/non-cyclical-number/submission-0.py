class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            current = n 
            temp = 0
            while current > 0:
                digit = current % 10
                temp += digit ** 2
                current //= 10
            n = temp
        return True