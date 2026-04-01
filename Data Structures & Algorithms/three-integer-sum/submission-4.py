class Solution:
    # i + j + k = 0
    # j+k = -i
    # time: O(n)
    # space: O(1) NOT INCLUDING SOLUTION
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(nlogn)

        resSet = set()
        for i in range(len(nums)-2):
            print(nums)
            j = i+1
            k = len(nums)-1
            while j < k:
                print(nums[i], nums[j], nums[k])
                jkSum = nums[j] + nums[k]
                if jkSum == -nums[i]:
                    triplet = sorted([nums[i], nums[j], nums[k]]) # O(nlogn) where n is always 3 so O(1)
                    resSet.add(tuple(triplet))
                    j += 1
                    k -= 1
                elif jkSum < -nums[i]:
                    j += 1
                else:
                    k -= 1
        
        return [list(triplet) for triplet in resSet]
