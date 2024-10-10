import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
largura_tela = 600
altura_tela = 400
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Define as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Define a posição e tamanho do objeto (um retângulo)
x = 300
y = 200
largura = 50
altura = 50
velocidade = 5

# Configura o relógio para controlar a taxa de atualização da tela
clock = pygame.time.Clock()

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Captura as teclas pressionadas
    teclas = pygame.key.get_pressed()

    # Movimenta o retângulo para cima ou para baixo
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_LEFT]:
        x -= velocidade

    # Preenche a tela com branco
    tela.fill(BRANCO)

    # Desenha o retângulo preto na nova posição
    pygame.draw.rect(tela, PRETO, (x, y, largura, altura))

    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de frames (60 fps)
    clock.tick(60)
