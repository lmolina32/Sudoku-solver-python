#!/usr/bin/env python3
from collections import defaultdict

class SudokuBoard:
    def __init__(self, grid=None):
        self.board = grid or [[0]*9 for _ in range(9)]
        self.size = 9

        self._normalize_board()

    def _normalize_board(self) -> None:
        '''Convert all empty cells into 0 for consistencty'''

        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0 or self.board[i][j] == '.':
                    self.board[i][j] = 0
                else:
                    self.board[i][j] = int(self.board[i][j])
        return

    def is_valid_move(self, row: int, col: int, num: int) -> bool:
        '''checks if num is a valid move on the board'''

        if num in self.board[row]:
            return False

        for i in range(9):
            if self.board[i][col] == num:
                return False

        sqr_row, sqr_col = (row // 3) * 3, (col // 3) * 3

        for i in range(sqr_row, sqr_row + 3):
            for j in range(sqr_col, sqr_col + 3):
                if num in self.board[i][j]:
                    return False

        return True

    def get_empty_cells(self) -> list:
        '''returns list of all the empty cells with the (cols, rows)'''

        empty = []

        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0 or self.board[i][j] == '.':
                    empty.append((i, j))
        return empty

    def solved(self) -> bool:
        '''checks if board is solved'''

        if len(self.get_empty_cells()):
            return False

        return self._is_sovled(self)

    def _is_solved(self) -> bool:
        '''helper function to determine if board is solved'''

        for row in self.board:
            if sorted(row) != list(range(1,10)):
                return False

        for col in range(9):
            cols = [self.board[row][col] for row in range(9)]
            if sorted(cols) != list(range(1,10)):
                return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        box.append(self.board[i][j])
                if sorted(box) != list(range(1,10)):
                    return False

        return True

    def set_cell(self, row: int, col: int, num: int) -> None:
        '''set cell with value'''
        self.board[row][col] = num
        return

    def get_cell(self, row: int, col: int) -> int
        '''return number in celll'''
        return self.board[row][col]

    def display(self) -> None:
        '''dispay board'''
        pass

    def __str__(self) -> None:
        '''print board with print statement'''
        pass


if __name__ == "__main__":
    pass
