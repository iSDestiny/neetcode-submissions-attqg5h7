class Solution:
    # i + j + k = 0
    # j+k = -i
    # time: O(n)
    # space: O(1) NOT INCLUDING SOLUTION
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(nlogn)

        resSet = []
        for i in range(len(nums)-2):
            print(nums)
            j = i+1
            k = len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while j < k:
                jkSum = nums[j] + nums[k]
                if jkSum == -nums[i]:
                    triplet = [nums[i], nums[j], nums[k]] 
                    resSet.append(triplet)
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1
                elif jkSum < -nums[i]:
                    j += 1
                else:
                    k -= 1
        
        return resSet
