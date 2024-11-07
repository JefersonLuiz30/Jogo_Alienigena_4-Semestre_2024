class Settings:
    # configuração fundo da tela
    def __init__(self):
        self.largura_tela = 1080
        self.altura_tela = 600
        self.bg_color = (230, 230, 230)

        self.velocidade_nave = 6.5

        # self.velocidade_nave=1.5
        self.nave_vida = 3

        # config das balas
        self.velocidade_missel = 10
        self.largura_missel = 3
        self.altura_missel = 15
        self.cor_missel = (255, 00, 00)
        self.disparos_por_vez = 10

        # COnfigurção do alien
        self.velocidade_alien = 1.0
        self.velocidade_frota = 5
        # direção da fila onde 1 representa direita; -1 representa esquerda
        self.direcao_frota = 1
