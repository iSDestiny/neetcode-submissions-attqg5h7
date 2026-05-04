import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        self.nums = nums
        while nums and len(self.nums) > k:
            heapq.heappop(self.nums)
        print(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        print(self.nums)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        print(self.nums)
        return self.nums[0]