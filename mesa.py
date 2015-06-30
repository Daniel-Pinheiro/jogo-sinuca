# -*- coding: utf8 -*-


import pygame
from FGAme import *
from random import uniform
import taco

# Inicializa o mundo

class Mesa(World):

    def __init__(self, gravity=0, restitution=1, num_balls=15, radius=10):

        super(Mesa, self).__init__(gravity=gravity, restitution=restitution, background = (0, 0, 0))

        # Variáveis funcionais
        self.clique = 0
        self.mouseX = 0
        self.mouseY = 0

        # Mesa (tamanho: 740 x 395)
        #   xi, xf, yi, yf 
        raio_buraco = 25

        self.table = AABB(30, 770, 100, 495, world=self, mass='inf', color=(0,146,64))
        AABB((30+raio_buraco), (400-raio_buraco), 495, 800, world=self, mass='inf', col_layer=1)  # Cima - Esquerda
        AABB((400+raio_buraco), (770-raio_buraco), 495, 800, world=self, mass='inf', col_layer=1) # Cima - Direita
        AABB(0, 30, (100+raio_buraco), (495-raio_buraco), world=self, mass='inf', col_layer=1)   # Esquerda
        AABB(770, 800, (100+raio_buraco), (495-raio_buraco), world=self, mass='inf', col_layer=1) # Direita
        AABB((30+raio_buraco), (400-raio_buraco), 0, 100, world=self, mass='inf', col_layer=1) # Baixo - Esquerda
        AABB((400+raio_buraco), (770-raio_buraco), 0, 100, world=self, mass='inf', col_layer=1) #Baixo - Direita 

        # Buracos da mesa
        pos_buracos = [(30, 495), (770, 495), (400, 495), (400, 100),(30, 100), (770, 100)]
        for pos in pos_buracos:
            buraco = Circle(radius=raio_buraco, vel=Vec2(0, 0), pos=Vec2(pos), mass='inf')
            self.add(buraco)
        
        # Inicia bolas
      
        # Vetor de posição das bolas        

        posX = 200
        posY = 297.5
        pos_bolas = [(posX,posY), (posX-20,posY-10), (posX-20,posY+10), (posX-40, posY-20), 
                    (posX-40, posY), (posX-40, posY+20), (posX-60, posY-30), (posX-60, posY-10),
                    (posX-60,posY+10), (posX-60, posY+30), (posX-80, posY-40), (posX-80, posY-20),
                    (posX-80, posY), (posX-80, posY+20), (posX-80, posY+40)]
    
        # Vetor de cores das bolas

        cor_bolas = [(255,255,0), (0,0,255), (255,0,0), (128,0,128), (255,20,147), (0,128,0), (244,164,96), (0,0,0),
                        (255,215,0), (0,0,205), (139,0,0), (34,139,34), (255,105,180), (138,43,226), (188,143,143)]

        # Na ordem: amarela, azul, vermelha, violeta, rosa, verde, bege, preta, 
        #           amarela, azul, vermelha, verde, rosa, violeta, bege
        
        #Cria as bolas e as associa com as posições e as cores:
        self.bolas = []
        for x in range (num_balls):
            bola = Circle(radius=radius, mass=1, col_layer=1)
            bola.pos = pos_bolas[x]
            bola.color = cor_bolas[x]
            self.bolas.append(bola)
            self.add(bola)

        # Define bola branca

        pos = (400,297.5)
        vel = (-150, 0)
        self.bolao = Circle(radius=1.5*radius, vel=(0, 0), pos=pos, mass=2, col_layer=1)
        self.bolao.color = (255,255,255)
        self.bolas.append(self.bolao)
        self.add(self.bolao)


        # Define objeto que representa a ponta do taco
        self.ponta = Circle(radius=2, vel=(0, 0), pos=(350,297.5), mass=2, col_layer=1)
        self.add(self.ponta)


    @listen('frame-enter')
    def bola_buraco(self):
        for b in self.bolas:
            if b.ymin > 495:
                b.pos = (400,400)
                self.remove(b)
            elif b.ymax < 100:
                b.pos = (400,400)
                self.remove(b)
            elif b.xmin > 770:
                b.pos = (400,400)
                self.remove(b)
            elif b.xmax < 30:
                b.pos = (400,400)
                self.remove(b)

    @listen('key-down', 'space')
    def toggle_pause(self):
        #super(Mesa, self).toggle_pause()  
        #Para testes apenas. Aperte espaço para dar uma velocidade aleatória à todas as bolas na mesa.
        for b in self.bolas:
            b.vel = (uniform(-250,250), uniform(250,-250))

    @listen('mouse-motion')
    def move_mouse(self, pos):
        self.mouseX = pos[0]
        self.mouseY = pos[1]

    @listen('mouse-button-down')
    def click_mouse (self, button, pos):
        
        for b in self.bolas:
            if button == 'left' and self.clique == 1:
                self.clique = 0
            elif button == 'left' :
                self.clique = 1
    
    @listen('post-draw')
    def draw_line (self, window):
        comprimento = 200
        coord_mouse = Vec2( self.mouseX, 600 - self.mouseY )
        coord_bola = Vec2( self.bolao.pos[0], 600 - self.bolao.pos[1] )

        direcao = coord_bola - coord_mouse
        direcao = direcao.normalize()
        
        pos_base = coord_mouse - direcao*20
        pos_ponta = pos_base + direcao*comprimento

        

        if (self.clique == 1):
            self.ponta.pos = (pos_ponta[0], -pos_ponta[1])
            pygame.draw.line(window._screen, (255,255,255), pos_base, pos_ponta, 5)

# Inicia o jogo

if __name__ == '__main__':
    w = Mesa()
    w.run()

