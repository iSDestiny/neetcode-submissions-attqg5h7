class Solution:
    # For each index in s decide:
    # - take only one digit
    # - take two digits, must be between 10 and 26 inclusive

    # Brute Force: Time: O(2^n)
    # DP Memoization: Time: O(n), Space: O(n)
    # DP Bottom Up
    # base case: dp[n] = 1
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        dp[len(s)] = 1

        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue
            dp[i] += dp[i+1]
            if i < len(s)-1 and int(s[i:i+2]) <= 26:
                dp[i] += dp[i+2]
        return dp[0]
