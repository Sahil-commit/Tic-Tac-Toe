import pygame

from board import Board
from settings import *


class Game:
    def __init__(self, screen):
        self.screen = screen

        # Create Board Object
        self.board = Board()

        # Current Player
        self.player = "X"

        # Game State
        self.running = True

    # -----------------------------
    # Handle Mouse / Keyboard Events
    # -----------------------------
    def handle_events(self, event):

        def handle_events(self, event):

    if event.type == pygame.MOUSEBUTTONDOWN:

        mouse_x, mouse_y = pygame.mouse.get_pos()

        row = mouse_y // CELL_SIZE
        col = mouse_x // CELL_SIZE

        if row < ROWS and col < COLS:

            if self.board.is_empty(row, col):

                self.board.place_mark(row, col, self.player)

                if self.board.check_winner(self.player):

                    print(f"{self.player} Wins!")

                elif self.board.is_full():

                    print("Draw!")

                if self.player == "X":
                    self.player = "O"
                else:
                    self.player = "X"
    # -----------------------------
    # Update Game
    # -----------------------------
    def update(self):

        pass

    # -----------------------------
    # Draw Everything
    # -----------------------------
    def draw(self):

        # Background
        self.screen.fill(BACKGROUND_COLOR)

        # Draw Board
        self.board.draw(self.screen)