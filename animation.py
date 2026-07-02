import pygame


class Animation:

    def __init__(self):

        self.alpha = 0

        self.finished = False

    def fade_in(self):

        if self.alpha < 255:
            self.alpha += 5
        else:
            self.finished = True

    def reset(self):

        self.alpha = 0

        self.finished = False

    def draw_overlay(self, screen):

        overlay = pygame.Surface(screen.get_size())

        overlay.set_alpha(self.alpha)

        overlay.fill((255, 255, 255))

        screen.blit(overlay, (0, 0))
