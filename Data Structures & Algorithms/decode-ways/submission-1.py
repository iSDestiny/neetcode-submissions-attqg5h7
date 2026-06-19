class Solution:
    # For each index in s decide:
    # - take only one digit
    # - take two digits, must be between 10 and 26 inclusive

    # Brute Force: Time: O(2^n)
    # DP Memoization: Time: O(n), Space: O(n)
    def numDecodings(self, s: str) -> int:
        cache = [-1] * len(s)
        def recurse(i: int) -> int:
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            if cache[i] > -1:
                return cache[i]
            
            single = recurse(i+1)
            double = 0
            if i < len(s)-1 and int(s[i:i+2]) <= 26:
                double = recurse(i+2)
            cache[i] = single + double
            return cache[i]
        return recurse(0)
