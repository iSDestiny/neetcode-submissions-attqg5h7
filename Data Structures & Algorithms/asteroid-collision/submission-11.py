class Solution:
    # Input: asteroids = [2,4,-4,-1]
    # Output: [2]
    #
    # Can use a stack:
    # - [2]
    # - output: [2]
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for rock in asteroids:
            while stack and rock < 0 and stack[-1] > 0:
                if stack[-1] < abs(rock):
                    stack.pop()
                elif stack[-1] == abs(rock):
                    stack.pop() 
                    rock = 0
                else:
                    rock = 0
            if rock:
                stack.append(rock)
        return stack
                 
