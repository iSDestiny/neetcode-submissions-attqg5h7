from collections import deque

class Solution:
    # perform a BFS starting from all the cells that touch the pacific and work up from there to mark all neighbors
    # that is reachable from this cells as touching the pacific, we do this by utilizing a pacific hashset. A neighbor
    # is reachable if the initial cell (i.e. 4) is <= the neighbor.
    # perform the same operation for all atlantic cells
    # after performing both BFS we will result in two hashsets: pacific and atlantic which will contain all the coords that 
    # touch pacific and atlantic, to get all the coords that touch both we just need to find all the coords that are in both sets
    #
    # Time: O(2(n*m)) -> O(n*m)
    # Space: O(3(n*m)) -> O(n*m)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])
        pqueue = deque()

        # get all the pacific touching coords
        for i in range(ROW):
            pqueue.append((i, 0))
        for i in range(COL):
            pqueue.append((0, i))

        aqueue = deque()
        # get all the atlantic touching coords
        for i in range(COL):
            aqueue.append((ROW-1, i))
        for i in range(ROW):
            aqueue.append((i, COL-1))
        
        def bfs(queue):
            visited = set(queue)

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while queue:
                i, j = queue.popleft()
                for di, dj in directions:
                    i2, j2 = i+di,j+dj 
                    if i2 < 0 or j2 < 0 or i2 >= ROW or j2 >= COL or (i2,j2) in visited or heights[i2][j2] < heights[i][j]:
                        continue
                    visited.add((i2,j2))
                    queue.append((i2, j2))
            return visited
        
        pacific = bfs(pqueue)
        atlantic = bfs(aqueue)

        res = []
        for item in pacific:
            i, j = item
            if item in atlantic:
                res.append([i,j]) 
        return res
