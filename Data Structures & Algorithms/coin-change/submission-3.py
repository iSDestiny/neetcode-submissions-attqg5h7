class Solution:
    # Time: O(n*t)
    # Space: O(t)
    # Top Down
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     cache = [-1] * (amount+1)
    #     def recurse(amt: int) -> int:
    #         if amt == 0:
    #             return 0
    #         if cache[amt] > -1:
    #             return cache[amt]
    #         count = 10000
    #         for i in range(len(coins)):
    #             if amt-coins[i] >= 0:
    #                 c = recurse(amt-coins[i])
    #                 count = min(count, 1+c)
    #         cache[amt] = count
    #         return cache[amt]
    #     c = recurse(amount) 
    #     return -1 if c == 10000 else c

    # Time: O(n*t)
    # Space: O(t)
    # Bottom Up
    # base case: 
    # dp[0] = 0
    # recurrence relation: f(amount) = min(f(amount-coins[i] for i in range(len(coins))))
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount+2)

        for a in range(1, amount+1):
            count = 10000
            for i in range(len(coins)):
                diff = a - coins[i]
                if diff >= 0:
                    c = dp[diff]
                    count = min(count, 1+c)
            dp[a] = count
        return -1 if dp[amount] == 10000 else dp[amount]