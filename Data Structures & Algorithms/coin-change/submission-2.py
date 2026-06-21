class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [-1] * (amount+1)
        def recurse(amt: int) -> int:
            if amt == 0:
                return 0
            if cache[amt] > -1:
                return cache[amt]
            count = 10000
            for i in range(len(coins)):
                if amt-coins[i] >= 0:
                    c = recurse(amt-coins[i])
                    count = min(count, 1+c)
            cache[amt] = count
            return cache[amt]
        c = recurse(amount) 
        return -1 if c == 10000 else c