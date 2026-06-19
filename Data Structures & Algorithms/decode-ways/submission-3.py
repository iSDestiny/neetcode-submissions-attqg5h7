class Solution:
    # For each index in s decide:
    # - take only one digit
    # - take two digits, must be between 10 and 26 inclusive

    # Brute Force: Time: O(2^n)
    # DP Memoization: Time: O(n), Space: O(n)
    # DP Bottom Up
    # base case: dp[n] = 1
    def numDecodings(self, s: str) -> int:
        first,second = 1, 0
        for i in range(len(s)-1, -1, -1):
            temp = 0
            if s[i] != "0":
                temp += first
                if i < len(s)-1 and int(s[i:i+2]) <= 26:
                    temp += second
            second = first
            first = temp 
        return first
