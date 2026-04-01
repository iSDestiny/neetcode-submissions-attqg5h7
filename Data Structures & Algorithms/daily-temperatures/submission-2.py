class Solution:
    # temps = [30,38,30,36,35,40,28] 
    # stack = [(40, 5), (28, 0)] 
    # result = [1, 4, 1, 2, 1, 0, 0]
    # Time: O(n)
    # Space: O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                index = stack.pop()[1]
                result[index] = i-index
            stack.append((temperatures[i], i))
        
        return result