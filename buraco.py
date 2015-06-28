# -*- coding: utf8 -*-
from FGAme import *

#  Esta classe serve para implementar melhor os buracos, pois quando são
#  apenas circulos, eles acabam colidindo com as bolas.
#
#  Um buraco é composto de três circulos,com um dentro do outro, onde o 
#  maior não possui colisão e tem o tamanho do buraco, o médio, ao colidir,
#  começa a atrair a bola e o menor, ao colidir, tira a bola de jogo e
#  incrementa um dos placares.

class Buraco(Circle):

    def __init__(self, pos=Vec2(0,0)):
        pass
