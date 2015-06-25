# -*- coding: utf8 -*-

from FGAme import *
from random import uniform, randint

# Inicializa o mundo


class Mesa(World):

    def __init__(self,
                 gravity=0, friction=0.5, restitution=0.95,
                 num_balls=16, speed=200, radius=10,
                 color='random'):
        '''Cria uma simulação de um gás de partículas confinado por um êmbolo
        com `num_balls` esferas de raio `radius` com velocidades no intervalo
        de +/-`speed`.'''

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
        self.bolas = []
        for _ in range(num_balls):
            pos = Vec2(uniform(50, 750), uniform(150, 450))
            vel = Vec2(uniform(-speed, speed), uniform(-speed, speed))
            bola = Circle(radius=radius, vel=vel, pos=pos, mass=1)
            bola.color = self.get_color(color)
            #self.bolas.append(bola)
            self.add(bola)
    
        pos = Vec2(uniform(50, 750), uniform(150, 450))
        bolao = Circle(radius=1.5*radius, vel=Vec2(0, 0), pos=pos, mass=2)
        bolao.color = (245, 245, 245)
        self.add(bolao)

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
