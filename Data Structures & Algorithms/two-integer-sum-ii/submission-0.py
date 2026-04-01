class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        aIndex = 0
        bIndex = len(numbers) - 1

        while aIndex < bIndex:
            abSum = numbers[aIndex] + numbers[bIndex]
            if abSum == target:
                return [aIndex+1, bIndex+1]
            elif abSum < target:
                aIndex += 1
            else:
                bIndex -=1
        return [0,0]
                