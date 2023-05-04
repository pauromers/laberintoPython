#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Habitacion(ElementoMapa):
    def __init__(self,num):
        self.num=num
        self.este=None
        self.oeste=None
        self.sur=None
        self.norte=None

    def entrar(self):
        print('Estas en la habitacion', str(self.num))
    
    # def get_este():
    #     return este
    
    # def get_norte():
    #     return norte
    
    # def get_sur():
    #     return sur
    
    # def get_oeste():
    #     return oeste