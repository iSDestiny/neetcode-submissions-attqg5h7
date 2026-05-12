from collections import deque

# Time: O(n*m)
# Space: O(n*m)
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        queue = deque()

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
        
        visited = set()
        while queue:
            i, j, distance = queue.popleft()
            if (i, j) in visited or i < 0 or j < 0 or i >= ROW or j >= COL:
                continue
            if grid[i][j] == -1:
                continue
            visited.add((i,j))
            if grid[i][j] > 0:
                grid[i][j] = distance
            # add all 4 directions
            queue.append((i+1, j, distance+1))
            queue.append((i-1, j, distance+1))
            queue.append((i, j+1, distance+1))
            queue.append((i, j-1, distance+1))
        
        