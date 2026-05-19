# target = numbers[index1] + numbers[index2], index1 < index2
#
# constraints:
# len(numbers) >= 2
# -inf <= numbers[i], target <= inf
# 
# time: O(n)
# space: O(1)


class Solution:
    # Input: numbers = [1,2,3,4], target = 3
    # Output: [1,2]
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1 # i = 0, 3

        while i < j: # 0 < 3, 0 < 2, 0 < 1
            curr_sum = numbers[i] + numbers[j] # numbers[0] + numbers[3] = 5, numbers[0] + numbers[2] = 4

            if curr_sum == target: # FALSE, ...
                return [i+1, j+1]
            elif curr_sum < target: # FALSE, ...
                i += 1
            else: # TRUE, TRUE
                j -= 1
        
        return []
            