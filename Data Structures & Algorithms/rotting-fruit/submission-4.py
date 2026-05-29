class Solution:
    # Time: O(m*n)
    # Space: O(m*n)
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # get the rotten oranges into queue
        ROW = len(grid)
        COL = len(grid[0])

        queue = deque()
        fruits = 0
        rotten = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    rotten += 1
                if grid[i][j] != 0:
                    fruits += 1
        
        if rotten == fruits:
            return 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        rounds = 0
        while queue:
            # only process fruits in this round
            processed = False
            for _ in range(len(queue)):
                i, j = queue.popleft()
                
                # process neighbors
                for di, dj in directions:
                    i2, j2 = i + di, j + dj
                    if i2 < 0 or j2 < 0 or i2 >= ROW or j2 >= COL:
                        continue
                    if grid[i2][j2] == 1:
                        queue.append((i2,j2))
                        grid[i2][j2] = 2
                        rotten += 1
            rounds += 1
        
        return rounds-1 if rotten == fruits else -1