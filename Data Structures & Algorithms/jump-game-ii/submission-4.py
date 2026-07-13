class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        count = 0
        while r + 1 < len(nums):
            last_index = -1
            first_index = -1
            for i in range(r, l-1, -1):
                new_last = i + nums[i] 
                if new_last > last_index:
                    last_index = new_last
                    first_index = i+1
            r = last_index
            l = first_index
            count += 1
        return count
