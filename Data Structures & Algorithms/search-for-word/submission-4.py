class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(i, j, c):
            if c == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[c] != board[i][j] or (i, j) in visited:
                return False
            visited.add((i, j))
            res = (dfs(i+1, j, c+1) or dfs(i-1, j, c+1) or dfs(i, j+1, c+1) or dfs(i, j-1, c+1))
            visited.remove((i,j))
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False

