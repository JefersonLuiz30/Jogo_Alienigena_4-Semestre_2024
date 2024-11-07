class Estatisticas:
    def __init__(self, ia_game):
        self.settings = ia_game.settings
        self.reset_estatisticas()

    def reset_estatisticas(self):
        self.naves_restantes = self.settings.nave_vida
