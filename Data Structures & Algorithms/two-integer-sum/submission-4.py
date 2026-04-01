class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # x + y = z -> y = z - x where z is the target
        indexes = dict()

        for i, n in enumerate(nums):
            indexes[n] = i
        
        for i, x in enumerate(nums):
            y = target - x
            if y in indexes and indexes[y] != i:
                return [i, indexes[y]]
        return []
