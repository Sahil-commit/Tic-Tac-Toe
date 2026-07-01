import pygame


class Button:

    def __init__(self, x, y, width, height, text, color, hover_color, font):

        self.rect = pygame.Rect(x, y, width, height)

        self.text = text

        self.color = color

        self.hover_color = hover_color

        self.font = font

    def draw(self, screen):

        mouse = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse):
            pygame.draw.rect(screen, self.hover_color, self.rect, border_radius=10)
        else:
            pygame.draw.rect(screen, self.color, self.rect, border_radius=10)

        text = self.font.render(self.text, True, (255, 255, 255))

        screen.blit(text, text.get_rect(center=self.rect.center))

    def is_clicked(self, event):

        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and self.rect.collidepoint(event.pos)
        )