#!/usr/bin/python
#-*- coding: utf-8 -*-

from Decorator import Decorator

class Bomba(Decorator):
    def __init__(self):
        self.activa =False
        self.esBomba=True

    def entrar(self):
        if self.activa:
            print('La bomba ha explotado')
            self.activa = False
        else:
            self.component.entrar()



