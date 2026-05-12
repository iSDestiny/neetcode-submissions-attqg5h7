from collections import deque

class Solution:
    # Time: O(n*m)
    # Space: O(n*m)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        queue = deque()        
        visited = set()

        total = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    total += 1
        
        minutes = 0
        directions = [(-1, 0), (1, 0), (0,-1), (0, 1)]
        while queue and total > 0:
            q = len(queue)
            for _ in range(q):
                i, j = queue.popleft()
                visited.add((i,j))
                for d in directions:
                    i2, j2 = i+d[0], j+d[1]
                    if i2 < 0 or j2 < 0 or i2 >= ROW or j2 >= COL or (i2, j2) in visited or grid[i2][j2] != 1:
                        continue
                    queue.append((i2,j2))
                    grid[i2][j2] = 2
                    total -= 1
            minutes += 1
        return minutes if total == 0 else -1