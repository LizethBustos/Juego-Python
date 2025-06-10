import pygame
import sys
from menu import mostrar_menu
from jugador import Jugador
from enemigo import Enemigo

def jugar():
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Escape del Laberinto")
    reloj = pygame.time.Clock()

    jugador = Jugador(100, 100)
    enemigos = [Enemigo(200, 200), Enemigo(400, 300), Enemigo(600, 100)]

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        teclas = pygame.key.get_pressed()
        jugador.mover(teclas)

        for enemigo in enemigos:
            enemigo.mover()

        pantalla.fill((0, 0, 0))
        jugador.dibujar(pantalla)
        for enemigo in enemigos:
            enemigo.dibujar(pantalla)
        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    mostrar_menu(jugar)
