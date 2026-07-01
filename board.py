import pygame
from settings import *


class Board:
    def __init__(self):
        self.board = [["" for _ in range(COLS)] for _ in range(ROWS)]

    def draw(self, screen):

        # Draw Grid
        for i in range(1, ROWS):
            pygame.draw.line(
                screen,
                GRID_COLOR,
                (0, i * CELL_SIZE),
                (WIDTH, i * CELL_SIZE),
                LINE_WIDTH
            )

        for j in range(1, COLS):
            pygame.draw.line(
                screen,
                GRID_COLOR,
                (j * CELL_SIZE, 0),
                (j * CELL_SIZE, HEIGHT),
                LINE_WIDTH
            )

        # Draw Symbols
        for row in range(ROWS):
            for col in range(COLS):

                x = col * CELL_SIZE
                y = row * CELL_SIZE

                if self.board[row][col] == "X":

                    pygame.draw.line(
                        screen,
                        X_COLOR,
                        (x + PADDING, y + PADDING),
                        (x + CELL_SIZE - PADDING, y + CELL_SIZE - PADDING),
                        SYMBOL_WIDTH,
                    )

                    pygame.draw.line(
                        screen,
                        X_COLOR,
                        (x + CELL_SIZE - PADDING, y + PADDING),
                        (x + PADDING, y + CELL_SIZE - PADDING),
                        SYMBOL_WIDTH,
                    )

                elif self.board[row][col] == "O":

                    pygame.draw.circle(
                        screen,
                        O_COLOR,
                        (x + CELL_SIZE // 2, y + CELL_SIZE // 2),
                        CELL_SIZE // 2 - PADDING,
                        SYMBOL_WIDTH,
                    )

    def is_empty(self, row, col):
        return self.board[row][col] == ""

    def place_mark(self, row, col, player):
        self.board[row][col] = player

    def is_full(self):
        for row in self.board:
            if "" in row:
                return False
        return True

    def check_winner(self, player):

        # Rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        # Columns
        for col in range(COLS):
            if all(self.board[row][col] == player for row in range(ROWS)):
                return True

        # Diagonal
        if all(self.board[i][i] == player for i in range(ROWS)):
            return True

        # Reverse Diagonal
        if all(self.board[i][ROWS - i - 1] == player for i in range(ROWS)):
            return True

        return False
