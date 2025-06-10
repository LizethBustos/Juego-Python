import pygame
import sys

def mostrar_menu(jugar_callback):
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    fuente = pygame.font.Font(None, 74)
    texto = fuente.render("Presiona ESPACIO para jugar", True, (255, 255, 255))
    rect = texto.get_rect(center=(400, 300))

    while True:
        pantalla.fill((0, 0, 0))
        pantalla.blit(texto, rect)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                jugar_callback()
                return
