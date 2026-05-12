from collections import defaultdict

class Solution:
    # Iterate through every row and check for duplicates utilizing a hashtable where we use a dict which will be used for duplicate checks
    # Iterate through every col and check for duplicates utilizing a hashtable where we use a dict which will be used for duplicate checks
    # Iterate through every sub-box and check for duplicates utilizing a hashtable where we use a dict which will be used for duplicate checks
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                r = i
                c = j
                b = (i//3) * 3 + (j//3)

                if board[i][j] in row[r] or board[i][j] in col[c] or board[i][j] in box[b]:
                    return False
                
                row[r].add(board[i][j])
                col[c].add(board[i][j])
                box[b].add(board[i][j])
        
        return True