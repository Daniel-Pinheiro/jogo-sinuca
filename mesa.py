# -*- coding: utf8 -*-
import sys
sys.path.append ('/home/lucas/workspace/FGAme/src/')
from FGAme import *
from random import uniform, randint

# Inicializa o mundo


class Mesa(World):

    def __init__(self,
                 gravity=0, friction=0.5, restitution=0.95,
                 num_balls=1, speed=200, radius=10,
                 color='random'):

        super(Mesa, self).__init__(gravity=gravity, dfriction=friction,
                                  restitution=restitution)

        self.background_color = (100, 245, 100)
        # Buracos da mesa
        pos_buracos = [(30, 495), (770, 495), (30, 100), (770, 100)]

        for pos in pos_buracos:
            buraco = Circle(radius=20, vel=Vec2(0, 0), pos=Vec2(pos), mass='inf')
            self.add(buraco)
        
        # Limites da mesa (740 x 395)
        #   xi, xf, yi, yf 
        jk = AABB(0, 800, 495, 800, world=self, mass='inf')  # Cima
        AABB(0, 30, 30, 800, world=self, mass='inf')   # Esquerda
        AABB(770, 800, 30, 800, world=self, mass='inf') # Direita
        AABB(0, 800, 0, 100, world=self, mass='inf')     # Baixo

        # Inicia bolas
        # Posição das bolas
        posX = 200
        posY = 297.5
        pos_bolas = [(posX,posY), (posX-20,posY-10), (posX-20,posY+10), (posX-40, posY-20), 
                    (posX-40, posY), (posX-40, posY+20), (posX-60, posY-30), (posX-60, posY-10),
                    (posX-60,posY+10), (posX-60, posY+30), (posX-80, posY-40), (posX-80, posY-20),
                    (posX-80, posY), (posX-80, posY+20), (posX-80, posY+40)]
        for pos in pos_bolas:
            vel = (0, 0)
            bola = Circle(radius=radius, vel=vel, pos=pos, mass=1)
            bola.color = self.get_color(color)
            self.add(bola)
    
        pos = Vec2(uniform(50, 750), uniform(150, 450))
        bolao = Circle(radius=1.5*radius, vel=Vec2(0, 0), pos=pos, mass=2)
        bolao.color = (0, 0, 0)
        #self.add(bolao)

    def get_color(self, color):
        if color == 'random':
            return (randint(0, 10)*25, randint(0, 10)*25, randint(0, 10)*25)
        else:
            return color

    @listen('key-down', 'space')
    def toggle_pause(self):
        super(Mesa, self).toggle_pause()

# Inicia o jogo
if __name__ == '__main__':
    w = Mesa()
    w.run()
