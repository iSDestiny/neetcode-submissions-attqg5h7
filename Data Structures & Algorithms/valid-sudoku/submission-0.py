class Solution:
    # row = [ {1,2,3}, {4,5}, {9}, {}, {}, {}, {}, {}, {}, {}]
    # col = [ {1,4}, {2,9}, {}, {5}, {3}, {}, {}, {}, {}, {3}]
    # sub = [ {1,2,4,9}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
    # O(n^2)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = [set() for i in range(len(board)+1)]
        colSet = [set() for i in range(len(board)+1)]
        subSet = [set() for i in range(len(board)+1)]

        for row in range(len(board)):
            for col in range(len(board)):
                cell = board[row][col]
                if not cell.isdigit():
                    continue
                subIndex = (row//3) * 3 + (col//3)
                if cell in rowSet[row] or cell in colSet[col] or cell in subSet[subIndex]:
                    return False
                rowSet[row].add(cell)
                colSet[col].add(cell)
                subSet[subIndex].add(cell)
                print(rowSet)
                print(colSet)
                print(subSet)
        
        return True
