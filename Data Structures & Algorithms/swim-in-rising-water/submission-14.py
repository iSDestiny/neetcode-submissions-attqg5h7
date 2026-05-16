from heapq import heappop, heappush

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        distances = {(i, j): float('inf') for i in range(ROW) for j in range(COL)}
        distances[(0,0)] = grid[0][0]
        heap = [(grid[0][0], 0, 0)]        

        directions = [(1, 0), (-1, 0), (0, 1), (0,-1)]
        while heap:
            d, i, j = heappop(heap)
            if d > distances[(i,j)]:
                continue
            
            if (i,j) == (ROW-1, COL-1): return d
            
            for di, dj in directions:
                i2,j2 = i+di, j+dj
                if i2 < 0 or j2 < 0 or i2 >= ROW or j2 >= COL: continue
                d2 = max(d, grid[i2][j2])
                if d2 < distances[(i2,j2)]:
                    distances[(i2,j2)] = d2
                    heappush(heap, (d2, i2, j2))
        
        return distances[(ROW-1, COL-1)]