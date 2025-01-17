from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.gameimage import *
from jogo import *
from mapa import *

#

class Menu:
    def __init__(self, janela, fundo):
        self.janela = janela
        self.fundo = fundo
        self.game = Game(self.janela)
        self.mapa = Mapa(self.janela)
        self.mouse = Mouse()
        self.counter = 0

        # assets
        self.fundo = GameImage("assets/fundo_menu.png")
        self.button = Sprite("assets/invaders_assets/button_1.jpg")
        self.button_start = Sprite("assets/invaders_assets/Start_button1.png")
        self.button_exit = Sprite("assets/invaders_assets/sair_button_1.jpg")


        # assets position
        menu_x = janela.width / 2 - self.button.width / 2
        menu_y = janela.height / 2 - self.button.height / 2

        self.button_start.x = menu_x
        self.button_start.y = menu_y

        self.button_exit.x = menu_x
        self.button_exit.y = menu_y + self.button.height + 25

    def menu_loop(self):
        while True:
            # cliques
            if self.mouse.is_over_object(self.button_exit) and self.mouse.is_button_pressed(1):
                break


            self.button_start = Sprite("assets/invaders_assets/Start_button1.png")
            self.button_start.x = self.janela.width / 2 - self.button.width / 2
            self.button_start.y = self.janela.height / 2 - self.button.height / 2

            if self.mouse.is_over_object(self.button_start):
                self.button_start = Sprite("assets/invaders_assets/Start_button3.png")
                self.button_start.x = self.janela.width / 2 - self.button.width / 2
                self.button_start.y = self.janela.height / 2 - self.button.height / 2

            if self.mouse.is_over_object(self.button_start) and self.mouse.is_button_pressed(1):
                # self.mapa.carrega_mapa()
                self.game.game_loop()



            self.fundo.draw()
            self.button_start.draw()
            self.button_exit.draw()
            self.janela.draw_text(f'pos : {self.mouse.get_position()}',  15, 15, size=20, color=(100, 100, 0))
            self.janela.update()

