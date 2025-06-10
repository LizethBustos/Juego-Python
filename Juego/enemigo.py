import pygame
import random

class Enemigo:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.color = (255, 0, 0)
        self.velocidad = 3
        self.direccion = random.choice([(1,0), (-1,0), (0,1), (0,-1)])

    def mover(self):
        self.rect.x += self.direccion[0] * self.velocidad
        self.rect.y += self.direccion[1] * self.velocidad

        if self.rect.left < 0 or self.rect.right > 800:
            self.direccion = (-self.direccion[0], self.direccion[1])
        if self.rect.top < 0 or self.rect.bottom > 600:
            self.direccion = (self.direccion[0], -self.direccion[1])

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, self.rect)
