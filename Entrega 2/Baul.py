#!/usr/bin/python
#-*- coding: utf-8 -*-

from Contenedor import Contenedor

class Baul(Contenedor):
    def __init__(self, num):
        self.num=num
    
    def entrar(self):
        print('Has encontrado el baul', str(self.num))
