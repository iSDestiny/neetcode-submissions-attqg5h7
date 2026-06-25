class Solution:
    # Brute Force:
    # Time: O(n^m+n)
    def change(self, amount: int, coins: List[int]) -> int:
        cache = [[-1]*(len(coins)+1) for _ in range(amount+1)]
        def recurse(target: int, i: int) -> int:
            if target < 0:
                return 0
            if target == 0:
                return 1
            if i >= len(coins):
                return 0
            if cache[target][i] > -1:
                return cache[target][i]
            c = coins[i]
            cache[target][i] = recurse(target-c, i) + recurse(target, i+1)
            return cache[target][i]
        
        return recurse(amount, 0)