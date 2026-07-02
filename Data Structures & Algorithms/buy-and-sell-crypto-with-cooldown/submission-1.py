# fn(i: int, price: int)
#   - base: i >= len(prices): return 0
#   - if neetcoin is owned:
#        - sell at the current index (total profit) + fn(i+2, 0)
#        - skip current: fn(i+1, price)
#        - return max of the first two options
#   - else:
#        - buy the current day: fn(i+1, prices[i])
#        - skip current day: fn(i+1, price)
#        - return max of first two options

# Time: O(2^n) -> O(n)
# Space: O(n) -> O(2n) -> O(n)
#
# [1,3,4,0,4]
#
# # fn(0, False) -> fn(1, True) -> fn(3, False)
#                               -> fn(2, True) 
#                -> fn(1, False)-> fn(2, True) X
#                               -> fn(2, False)

class Solution:

    def maxProfit(self, prices: List[int]) -> int:#          
        cache = {} # key: (i: int, own: bool)
        def recurse(i: int, own: bool) -> int: 
            if i >= len(prices):
                return 0
            if (i, own) in cache:
                return cache[(i, own)]
            if own:
                sell = prices[i] + recurse(i+2, False) 
                skip = recurse(i+1, own)
                cache[(i, own)] = max(sell, skip)
                return cache[(i,own)]
            
            buy = recurse(i+1, True) - prices[i]
            skip = recurse(i+1, own)
            cache[(i,own)] = max(buy, skip)
            return cache[(i,own)]
        
        return recurse(0, False)
            