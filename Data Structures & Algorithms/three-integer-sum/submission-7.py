# [-1,0,1,2,-1,-4] -> sorted -> [-4, -1, -1, 0, 1, 2] triplets = [[-1,-1,2]]
#                                    i   j         k == 0
# O(nlogn + n^2) -> O(n^2)
# Space: O(1)
# constraint:
# nums.length >= 3
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        res = []
        for i in range(len(nums)-2):
            # skip duplicates
            if i > 0 and nums[i-1] == nums[i]:
                continue

            j,k = i+1, len(nums)-1
            while j < k:
                #skip duplicates
                while j > i+1 and nums[j-1] == nums[j]:
                    j += 1
                # while k < len(nums)-1 and nums[k+1] == nums[k]:
                #     k -= 1
                if j >= k:
                    break

                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif curr_sum < 0:
                    j += 1
                else:
                    k -= 1
        return res
