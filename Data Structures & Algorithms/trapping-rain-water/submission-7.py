class Solution:
    # Two pointer approach
    # 
    # area for each position is bound by the lesser of the two peaks
    # Time: O(n)
    # Space: O(1)
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        l = 0
        r = len(height)-1

        leftMax = height[0]
        rightMax = height[-1]

        area = 0
        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                area += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                area += rightMax - height[r]
        return area