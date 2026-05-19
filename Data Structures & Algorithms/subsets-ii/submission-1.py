class Solution:
    # nums = [1,2,1] -> [1,1,2]
    #              2
    #            [1,2] -> END
    #              1
    #      [1] -> [1,1] -> [1,1,2]
    # [] 
    #      [2]   
    #
    # backtracking
    # Time: O(n*2^n)
    # Space: O(n) recursive stack
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # [1,2,1] -> [1,1,2]
        nums.sort()
        res = [] # []
        current = [] # []
        def dfs(start: int): # 0, 1, 2, 3 -> backtrack to 1
            res.append(current[::]) # res = [[], [1], [1,1], [1,1,2]]
            for i in range(start, len(nums)): # 0 -> 2, 1->2, 2->2, 3 > 2 [no loop]
                # skip duplicates
                if i > start and nums[i] == nums[i-1]: # FALSE, FALSE, FALSE
                    continue
                current.append(nums[i]) # current = [1], [1,1], [1,1,2]
                dfs(i+1) # dfs(1), dfs(2), dfl(3), dfs(2)
                current.pop() # current = [], [1], [1,1]
        dfs(0)
        return res