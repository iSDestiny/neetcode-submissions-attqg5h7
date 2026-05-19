class Solution:
    # area[i] = min(highestLeftHeight, highestRightHeight) - height[i]
    # 
    # Time: O(Kn) -> O(n)
    # Space: O(n)
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        leftMax,rightMax = 0,0
        area = 0
        while l < r:
            leftMax = max(leftMax, height[l]) 
            rightMax = max(rightMax, height[r])

            if leftMax < rightMax:
                area += leftMax - height[l]
                l += 1
            else:
                area += rightMax - height[r]
                r -= 1
        return area