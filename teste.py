import pygame

pygame.init()
tela = pygame.display.set_mode((400, 300))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()