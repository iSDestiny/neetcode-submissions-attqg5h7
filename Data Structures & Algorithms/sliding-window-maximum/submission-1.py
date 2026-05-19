from heapq import heappush, heappop
from collections import deque

class Solution:
    # Time: O(nlogk) if k = n then O(nlogn)
    # Space: O(n)
    #
    # Maintain a max heap where top of the heap is the max value seen so far,
    # if the top of the heap goes out of range of the window pop until the max is in the window
    #
    # What happens if len(nums) < k? Don't add max to list
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     heap = [] # (nums[i], index)
    #     res = []

    #     for j in range(len(nums)):
    #         heappush(heap, (-nums[j], j))
    #         if j < k-1: # window is smaller than k
    #            continue 
            
    #         while heap and heap[0][1] < j - k + 1: # max out of range then pop it until its in range
    #             heappop(heap)
            
    #         res.append(-heap[0][0])
    #     return res

    # monotonic queue
    # Time: O(n)
    # Space: O(n)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        for j in range(len(nums)):
            while queue and queue[-1][0] < nums[j]:
                queue.pop()
            queue.append((nums[j], j))

            if j < k-1: # window is smaller than k
                continue
            while queue and queue[0][1] < j -k +1: # max out of range, deque until its in range
                queue.popleft()
            res.append(queue[0][0]) 
        return res
