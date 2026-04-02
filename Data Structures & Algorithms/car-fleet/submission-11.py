import math

class Solution:
    # Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
    # descPos = [(7,1), (4,2), (1,2), (0,1)]
    # stack = [(7,1), (1,2), (0,1)]
    # output = 3
    #
    # Time: O(nlogn) + O(n) = O(nlogn)
    # Space: O(n)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        descPos = [(position[i], speed[i]) for i in range(len(position))]
        descPos.sort(reverse=True)
        stack = []
        print(descPos)
        for p, s in descPos:
            if stack:
                pp, ps = stack[-1]
                currentTime = float(target-p) / s
                prevTime = float(target-pp) / ps
                if prevTime < currentTime:
                    stack.append((p,s))
            else:
                stack.append((p,s))
            
        return len(stack)