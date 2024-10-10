import pygame
from pygame.sprite import Sprite

class Missel(Sprite):
    # Classe que representa um míssel disparado pela nave, herda de Sprite
    
    def __init__(self, ia_game):
        # Inicializa o míssel e define sua posição inicial
        super().__init__()  # Chama o construtor da classe mãe (Sprite)
        self.screen = ia_game.screen  # Obtém a tela de jogo para onde o míssel será desenhado
        self.settings = ia_game.settings  # Acessa as configurações do jogo, incluindo velocidade e cor do míssel
        self.color = self.settings.cor_missel  # Define a cor do míssel a partir das configurações
        
        # Cria um retângulo para o míssel na tela
        # O tamanho do míssel (largura e altura) é obtido das configurações
        self.rect = pygame.Rect(0, 0, self.settings.largura_missel, self.settings.altura_missel)
        
        # Coloca o míssel no topo da nave, na mesma posição horizontal
        self.rect.midtop = ia_game.nave.rect.midtop
        
        # Armazena a posição vertical do míssel como um valor decimal (float)
        self.y = float(self.rect.y)
        
    def update(self):
        # Atualiza a posição do míssel na tela (movimentação para cima)
        self.y -= self.settings.velocidade_missel  # Subtrai a velocidade da posição y, fazendo o míssel subir
        self.rect.y = self.y  # Atualiza a posição do rect (retângulo) do míssel com o novo valor y

    def gerar_missel(self):
        # Desenha o míssel na tela com as propriedades de cor e localização
        pygame.draw.rect(self.screen, self.color, self.rect)
