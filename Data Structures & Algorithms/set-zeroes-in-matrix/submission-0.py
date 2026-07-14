#   [1,2,3],
#   [4,0,5],
#   [6,7,8]
#
#
#   [1,2,3],
#   [4,0,5],
#   [6,7,8]
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW = len(matrix)
        COL = len(matrix[0])

        rowzero = [False] * ROW
        colzero = [False] * COL

        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    rowzero[r] = True
                    colzero[c] = True
        
        for r in range(ROW):
            for c in range(COL):
                if rowzero[r] or colzero[c]:
                    matrix[r][c] = 0
        
        
        