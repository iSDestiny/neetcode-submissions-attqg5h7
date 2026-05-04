import heapq

# We would use a max heap data structure.
# Run heapify on the initial list O(n)
# Then to run the simulation, each step take the two heaviest by
# popping from the max heap and then subtracting the second heaviest
# from the heaviest, if it's greater than 0 then add the difference back
# to the stones array else don't, repeat this until one more or no stones are remaining
# Time: O(nlogn)
# Space: O(1) extra space since we're using the input array as the heap itself
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones] # python only supports min heap
        heapq.heapify(stones) # O(n)
        
        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            newStone = y - x

            if newStone > 0:
                heapq.heappush(stones, -newStone)
        
        return 0 if len(stones) == 0 else -stones[0]