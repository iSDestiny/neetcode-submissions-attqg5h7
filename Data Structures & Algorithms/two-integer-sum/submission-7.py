
class Solution:
    # nums[i] + nums[j] == target where i != j
    # nums[i] = target - nums[j]
    # hash = {3: 0, 4: 1, 5: 2, 6: 3}
    # every input has exactly one pair of indices = this means there is only one answer
    # Time: O(n)
    # Space: O(n)
    # constraints:
    # -10000 <= nums[i], target <= 10000
    # 2 <= len(nums)

    def twoSum(self, nums: List[int], target: int) -> List[int]: # nums: [4,5,6], target: 10, output: [0,2]
        numDict = {} # {4: 0, 5: 1}
        for j in range(len(nums)): # 0, 1, 2
            val_i = target - nums[j] # 6 = 10 - 4, 5 = 10 - 5, 4 = 10-6
            if val_i in numDict: # False, False, True
                return [numDict[val_i], j] # [0, 2]
            numDict[nums[j]] = j # numDict[4] = 0, numDict[5] = 1
        
        # not possible since we're guaranteed at least one correct pair
        return []
                