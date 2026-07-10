class Solution:
    # Time: O(n)
    # Space: O(1)
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        goal = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        
        return goal == 0