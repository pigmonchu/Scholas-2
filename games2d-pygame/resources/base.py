# Importacion de los módulos
import pygame as pg
from pygame.locals import *
import sys
from entities import * #Clases necesarias para el juego

FPS = 60

class Game:
    clock = pg.time.Clock()

    def __init__(self, width, height):
        self.size = (width, height)
        self.display = pg.display
        self.screen = self.display.set_mode(self.size)
        self.display.set_caption('Pong')

# Entidades del juego, jugadores, enemigos,
# obstáculos…
    # …
    def handleEvent(self):
            for event in pg.event.get():
                if event.type == QUIT:
                        return False

        keys_pressed = pg.key.get_pressed()
        return True

    def mainloop(self):
        self.clock.tick(FPS)
    
            if not self.handleEvent():
                return False

        ''' Cambios del juego según se avanza (mecánica)'''
    …
            self.display.flip() # Repintado
            return True

    def start(self):
        while self.mainloop():
            pass
        self.game_over()
        
    def game_over(self):
            pg.quit()
            sys.exit()

if __name__ == '__main__':
    pg.init()
    game = Game(800, 600)
    game.start()
