import heapq

class KthLargest:

    # Time: O(nlogk)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        self.nums = nums
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    # Time: O(logk)
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]