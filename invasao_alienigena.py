import sys
from time import sleep
import pygame

from settings import Settings
from nave import Nave
from missel import Missel
from alien import Alien
from estatisticas import Estatisticas


class InvasaoAlienigena:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.jogo_ativo = True

        self.screen = pygame.display.set_mode(
            (self.settings.largura_tela, self.settings.altura_tela))
        pygame.display.set_caption("Invasão Alienígena")
        self.estatisticas = Estatisticas(self)

        # Carregar a imagem de fundo
        self.fundo = pygame.image.load('imagens/galaxy.jpg')

        self.nave = Nave(self)
        self.missel = pygame.sprite.Group()
        self.alien = pygame.sprite.Group()
        self._criar_frota()

    def jogo_on(self):
        while True:
            self._checar_eventos()
            if self.jogo_ativo:
                self.nave.update()
                self._atualiza_missel()
                self._atualiza_alien()
                self._atualiza_tela()
                self.clock.tick(60)

    def _checar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._checar_teclaspress_eventos(event)
            elif event.type == pygame.KEYUP:
                self._checar_soltarteclas_eventos(event)

    def _checar_teclaspress_eventos(self, event):
        if event.key == pygame.K_RIGHT:
            self.nave.mover_direita = True
        elif event.key == pygame.K_LEFT:
            self.nave.mover_esquerda = True
        elif event.key == pygame.K_UP:
            self.nave.mover_cima = True
        elif event.key == pygame.K_DOWN:
            self.nave.mover_baixo = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._disparar_missel()

    def _checar_soltarteclas_eventos(self, event):
        if event.key == pygame.K_RIGHT:
            self.nave.mover_direita = False
        elif event.key == pygame.K_LEFT:
            self.nave.mover_esquerda = False
        elif event.key == pygame.K_UP:
            self.nave.mover_cima = False
        elif event.key == pygame.K_DOWN:
            self.nave.mover_baixo = False

    def _batidas_naves(self):
        # reduz uma vida
        if self.estatisticas.naves_restantes > 0:
            self.estatisticas.naves_restantes -= 1
            # descarte os mísseis e naves que restarem
            self.missel.empty()
            self.alien.empty()
            # reinicia o jogo com a nave no centro
            self._criar_frota()
            self.nave.centraliza_nave()
            # faz uma pausa
            sleep(0.5)
        else:
            self.jogo_ativo = False

    def _disparar_missel(self):
        if len(self.missel) < self.settings.disparos_por_vez:
            novo_missel = Missel(self)
            self.missel.add(novo_missel)

    def _atualiza_missel(self):
        self.missel.update()
        for missel in self.missel.copy():
            if missel.rect.bottom <= 0:
                self.missel.remove(missel)

            colisao = pygame.sprite.groupcollide(
                self.missel, self.alien, True, True)

        self._checar_misseis_colididos()

    def _checar_misseis_colididos(self):
        colisao = pygame.sprite.groupcollide(
            self.missel, self.alien, True, True)
        if not self.alien:
            self.missel.empty()
            self._criar_frota()

    def _atualiza_alien(self):
        self._checar_frota_borda()
        self.alien.update()

        if pygame.sprite.spritecollideany(self.nave, self.alien):
            self._batidas_nave()
            self._checar_alien_final_tela()

    def _checar_alien_final_tela(self):
        for alien in self.alien.sprites():
            if alien.rect.bottom >= self.settings.altura_tela:
                self._batidas_nave()  # trata como se a nave fosse abatida
            break

    def _criar_frota(self):
        alien = Alien(self)
        self.alien.add(alien)
        alien_largura, alien_altura = alien.rect.size

        current_x, current_y = alien_largura, alien_altura
        while current_y < (self.settings.altura_tela - 4 * alien_altura):
            while current_x < (self.settings.largura_tela - 4 * alien_largura):
                self._criar_alien(current_x, current_y)
                current_x += 2 * alien_largura

            current_x = alien_largura
            current_y += 1 * alien_altura

    def _criar_alien(self, x_position, y_position):
        novo_alien = Alien(self)
        novo_alien.x = x_position
        novo_alien.rect.x = x_position
        novo_alien.rect.y = y_position
        self.alien.add(novo_alien)

    def _checar_frota_borda(self):
        for alien in self.alien.sprites():
            if alien.checar_borda():
                self._muda_direcao_frota()
                break

    def checar_borda(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0  )

    def update(self):
        self.x += self.settings.velocidade_alien*self.settings.direcao_frota
        self.rect.x = self.x

    def _muda_direcao_frota(self):
        for alien in self.alien.sprites():
            alien.rect.y += self.settings.velocidade_frota
            self.settings.direcao_frota *= -1.2
            break

    def _atualiza_tela(self):
        # Desenhar o fundo
        self.screen.blit(self.fundo, (0, 0))
        # Desenhar a nave
        self.nave.blitme()
        # Desenhar os aliens
        self.alien.draw(self.screen)
        # Atualizar a tela

        for missel in self.missel.sprites():
            missel.gerar_missel()

        pygame.display.flip()


if __name__ == '__main__':
    ia = InvasaoAlienigena()
    ia.jogo_on()
