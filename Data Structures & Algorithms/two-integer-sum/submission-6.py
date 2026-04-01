class Solution:

    # nums[i] + nums[j] == target
    # x + y = z
    # y = z - x <- to get the index of y we will use a hashtable where numbers in nums is the key and index is the value
    # x = current number in the iteration
    # z = target
    # NOTE: i != j so make sure the index of x doesn't equal to index of y
    # O(n) solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexDict = {}
        for i in range(len(nums)):
            indexDict[nums[i]] = i
        
        for i in range(len(nums)):
            x = nums[i]
            z = target
            y = z - x
            if y in indexDict:
                yIndex = indexDict[y]

                if i != yIndex:
                    return [i, yIndex]
        
        return [0,0]