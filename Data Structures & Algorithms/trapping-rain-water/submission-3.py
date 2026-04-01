class Solution:
    def trap(self, height: List[int]) -> int:
        prefixLeftMax = [0] * len(height)
        prefixRightMax = [0] * len(height)

        leftMax = 0
        for i in range(len(height)):
            prefixLeftMax[i] = leftMax
            leftMax = max(leftMax, height[i])
        rightMax = 0
        for i in range(len(height)-1, -1, -1):
            prefixRightMax[i] = rightMax
            rightMax = max(rightMax, height[i])
        
        print(prefixLeftMax)
        print(prefixRightMax)
        area = 0
        for i in range(len(height)):
            currSum = min(prefixLeftMax[i], prefixRightMax[i]) - height[i]
            if currSum > 0:
                area += currSum
        
        return area