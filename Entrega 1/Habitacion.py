#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Habitacion(ElementoMapa):
    def __init__(self,num):
        self.num=num

    def entrar(self):
        print('Estas en la habitacion', str(self.num))

