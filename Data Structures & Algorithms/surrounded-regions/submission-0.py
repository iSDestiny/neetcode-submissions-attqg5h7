from collections import deque

class Solution:
    # Time: O(n*m)
    # Space: O(n*m)
    def solve(self, board: List[List[str]]) -> None:
        queue = deque()
        ROW = len(board)
        COL = len(board[0])

        # get all border 'O's
        for i in range(ROW):
            if board[i][0] == "O":
                queue.append((i, 0))
            if board[i][COL-1] == "O":
                queue.append((i, COL-1))
        for j in range(COL):
            if board[0][j] == "O":
                queue.append((0, j))
            if board[ROW-1][j] == "O":
                queue.append((ROW-1, j))
        
        visited = set(queue)
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while queue:
            i, j = queue.popleft()
            for di, dj in directions:
                i2, j2 = i+di, j+dj
                if i2 < 0 or j2 < 0 or i2 >= ROW or j2 >= COL or (i2,j2) in visited or board[i2][j2] != "O":
                    continue
                visited.add((i2,j2))
                queue.append((i2,j2))
        
        for i in range(ROW):
            for j in range(COL):
                if (i,j) in visited:
                    continue
                board[i][j] = "X"