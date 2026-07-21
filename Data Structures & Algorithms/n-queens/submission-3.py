# Time: O(n!)
# Space: O(n^2)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        placed_col = set()
        placed_diag = set()
        placed_anti = set()

        board = []
        res = []

        def placequeen(col: int):
            return ("." * col) + "Q" + ("." * (n-col-1))

        def recurse(row: int):
            if row >= n:
                res.append(board[:])
                return
            for col in range(n): 
                # check if we can place it here
                if col in placed_col or row-col in placed_diag or row+col in placed_anti:
                    continue

                # place the queen and recurse on the next row
                placed_col.add(col)
                placed_diag.add(row-col)
                placed_anti.add(row+col)
                board.append(placequeen(col))

                recurse(row+1)

                # backtrack when done
                placed_col.remove(col)
                placed_diag.remove(row-col)
                placed_anti.remove(row+col)
                board.pop()
        recurse(0)

        return res