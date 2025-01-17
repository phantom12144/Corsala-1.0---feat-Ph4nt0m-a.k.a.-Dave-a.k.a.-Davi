import csv

import mapa
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.animation import *


class Game:
    def __init__(self, janela):
        self.janela = janela
        self.teclado = Keyboard()

        # carrega o mapa
        self.mapa = mapa.Mapa(self.janela)

        # gameimages
        self.fundo = GameImage("assets/fundo_preto.png")

        # sprites
        self.player = Sprite("assets/player_frente.png", True, 0, 4)
        # self.player.stop()
        # self.player.play()

        # posições
        self.player.x = self.janela.width/2 - self.player.width
        self.player.y = self.janela.height/2 - self.player.height

        self.mapa.carrega_mapa()

    def game_loop(self):
        while True:
            if self.teclado.key_pressed("ESC"):
                break

            self.mapa.move_player(self.player)

            self.fundo.draw()

            self.mapa.desenha_layer(0)

            self.mapa.desenha_layer(1)

            self.player.draw()
            # if self.player.is_playing():
            #     self.player.draw()
            #     self.player.update()

            self.mapa.desenha_layer(2)

            self.janela.update()
