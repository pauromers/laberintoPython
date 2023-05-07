#!/usr/bin/python
#-*- coding: utf-8 -*-

from Decorator import Decorator

class Fuego(Decorator):
    def __init__(self):
        self.activo =False
        self.esFuego=True

    def entrar(self):
        if self.activo:
            print('Te has quemado')
            self.activo = False
        else:
            self.component.entrar()



     