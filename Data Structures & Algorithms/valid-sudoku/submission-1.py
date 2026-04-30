class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue 
                box_number = (r // 3) * 3 + (c // 3)

                if board[r][c] in row[r] or board[r][c] in column[c] or board[r][c] in box[box_number]:
                    return False 
                else:
                    row[r].add(board[r][c])
                    column[c].add(board[r][c])
                    box[box_number].add(board[r][c])
        return True 






               
            





        