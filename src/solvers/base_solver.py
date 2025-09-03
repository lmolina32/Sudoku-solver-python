#!/usr/bin/env python3

from src.sudoku_board import SudokuBoard

def base_solver(board: SudokuBoard, row: int, col: int):
    ''' base solver using backtracking and recursion'''
    if row == 8 and col == 9:
        return True

    if col == 9:
        row += 1
        col = 0

    if board[row][col] != 0:
        return base_solver(board, row, col + 1)

    for num in range(1, 10):

        if board.is_valid_move(row, col, num):
            board[row][col] = num

            if base_solver(board, row, col + 1):
                return True
            board[row][col] = 0

    return False
