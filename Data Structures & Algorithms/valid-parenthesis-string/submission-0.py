class Solution:
    def checkValidString(self, s: str) -> bool:
        cache = [[-1]*len(s) for _ in range(len(s))]
        def recurse(i: int, left: int) -> bool:
            if i == len(s):
                return left == 0
            if left < 0:
                return False
            if cache[i][left] != -1:
                return cache[i][left]
            if s[i] == "(":
                cache[i][left] = recurse(i+1, left+1)
            if s[i] == ")":
                cache[i][left] = recurse(i+1, left-1)
            if s[i] == "*":
                cache[i][left] = recurse(i+1, left+1) or recurse(i+1, left-1) or recurse(i+1, left)
            return cache[i][left]
        return recurse(0,0) 