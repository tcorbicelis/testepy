import pygame
import random

pygame.init()

# Tela
LARGURA, ALTURA = 600, 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Cobrinha com Pontuação")

clock = pygame.time.Clock()

# Cores
PRETO = (0,0,0)
VERDE = (0,255,0)
VERMELHO = (255,0,0)
BRANCO = (255,255,255)

# Fonte padrão
fonte = pygame.font.Font(None, 30)

# Cobra e comida
cobra = [(100,100), (80,100), (60,100)]
direcao = "RIGHT"
comida = (random.randrange(0,LARGURA,20), random.randrange(0,ALTURA,20))

pontuacao = 0
velocidade = 10
TAMANHO = 20

def desenhar_cobra():
    for s in cobra:
        pygame.draw.rect(tela, VERDE, (s[0], s[1], TAMANHO, TAMANHO))

def mostrar_pontuacao():
    texto = fonte.render(f"Pontuação: {pontuacao}", True, BRANCO)
    tela.blit(texto, (10,10))

def mover_cobra():
    global pontuacao, comida
    x,y = cobra[0]
    global direcao
    if direcao == "UP": y -= TAMANHO
    elif direcao == "DOWN": y += TAMANHO
    elif direcao == "LEFT": x -= TAMANHO
    elif direcao == "RIGHT": x += TAMANHO
    nova = (x,y)
    if x<0 or x>=LARGURA or y<0 or y>=ALTURA or nova in cobra:
        return False
    cobra.insert(0,nova)
    if nova==comida:
        pontuacao+=1
        comida = (random.randrange(0,LARGURA,TAMANHO), random.randrange(0,ALTURA,TAMANHO))
    else:
        cobra.pop()
    return True

# Loop principal
while True:
    tela.fill(PRETO)
    for e in pygame.event.get():
        if e.type == pygame.QUIT: exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w and direcao!="DOWN": direcao="UP"
            elif e.key == pygame.K_s and direcao!="UP": direcao="DOWN"
            elif e.key == pygame.K_a and direcao!="RIGHT": direcao="LEFT"
            elif e.key == pygame.K_d and direcao!="LEFT": direcao="RIGHT"
    if not mover_cobra(): break
    desenhar_cobra()
    pygame.draw.rect(tela, VERMELHO, (comida[0], comida[1], TAMANHO, TAMANHO))
    mostrar_pontuacao()
    pygame.display.update()
    clock.tick(velocidade)

pygame.quit()