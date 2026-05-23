
# [7,1,7,2,2,4]

# *.  *
# *.  *
# *.  *
# *.  *.    *
# *.  *.    *
# *   * * * *
# * * * * * *
#
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            index = i
            while stack and stack[-1][1] > h:
                top_index, top_height = stack.pop()
                index = top_index 
                max_area = max(max_area, (i-top_index) * top_height)
            # if stack and stack[-1][1] == h:
            #     index = stack[-1][0]
            stack.append((index, h))

        while stack:
            top_index, top_height = stack.pop() 
            width = len(heights)-top_index
            area = top_height * width

            max_area = max(max_area, area)
        
        return max_area