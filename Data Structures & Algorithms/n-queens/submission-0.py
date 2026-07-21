class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        placed = set()
        board = []
        res = []

        def placequeen(col: int):
            row = ["."]*n
            row[col] = "Q"

            return "".join(row)

        def recurse(row: int):
            if row >= n:
                if len(placed) == n:
                    print(board)
                    res.append(board[:])
                return
            for col in range(n):
                # check if we can place it here
                canPlace = True
                for i,j in placed: # check placed queens
                    # check vertical and diagonal
                    if col == j or (abs(row-i) == abs(col-j)):
                        canPlace = False
                        break

                # place the queen and recurse on the next row
                if canPlace:
                    placed.add((row,col))
                    board.append(placequeen(col))
                    recurse(row+1)

                    # backtrack when done
                    placed.remove((row,col))
                    board.pop()
        recurse(0)

        return res