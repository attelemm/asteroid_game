from circleshape import CircleShape, PLAYER_RADIUS
import constants
import pygame

class Player(CircleShape):
    def __init__(self, x_cord, y_cord):
        super().__init__(x_cord, y_cord, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        self.screen = screen
        pygame.draw.polygon(self.screen, "white", self.triangle(), constants.LINE_WIDTH)
