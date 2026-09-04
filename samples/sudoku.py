def solve_sudoku(board):
    def is_valid(num, row, col):
        # Check row, column, and 3x3 subgrid
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3*(row//3), 3*(col//3)
        for i in range(start_row, start_row+3):
            for j in range(start_col, start_col+3):
                if board[i][j] == num:
                    return False
        return True

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    for num in range(1, 10):
                        if is_valid(num, r, c):
                            board[r][c] = num
                            if backtrack():
                                return True
                            board[r][c] = 0
                    return False
        return True

    backtrack()
    return board
