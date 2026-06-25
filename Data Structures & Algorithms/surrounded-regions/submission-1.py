from collections import deque
class Solution:
    # Time: O(m*n)
    # Space: O(m*n)
    def solve(self, board: List[List[str]]) -> None:
        ROW = len(board)
        COL = len(board[0])
        queue = deque()
        for j in range(COL):
            if board[0][j] == "O":
                queue.append((0, j))
            if board[ROW-1][j] == "O":
                queue.append((ROW-1, j))
        
        for i in range(ROW):
            if board[i][0] == "O":
                queue.append((i, 0))
            if board[i][COL-1] == "O":
                queue.append((i, COL-1))
        
        visited = set()
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        while queue:
            r1,c1 = queue.popleft()
            board[r1][c1] = "S"
            visited.add((r1,c1))
            for dr, dc in dirs:
                r2,c2 = r1+dr, c1+dc
                if (r2,c2) in visited or r2 < 0 or c2 < 0 or r2 >= ROW or c2 >= COL:
                    continue
                if board[r2][c2] == "O":
                    queue.append((r2,c2))
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] = "O"
                
