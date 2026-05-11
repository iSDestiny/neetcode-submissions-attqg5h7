class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        def dfs(start, path):
            res.append(path)
            for i in range(start, len(nums)):
                if i > start and nums[i-1] == nums[i]:
                    continue
                dfs(i+1, path + [nums[i]])
        dfs(0, [])
        return res