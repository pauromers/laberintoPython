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
        self.hijos = []

    def entrar(self):
        print('Estas en la habitacion', str(self.num)) 
    
    def obtenerHijos(self):
        return self.hijos
    
    def agregarHijo(self, unHijo):
        self.hijos.append(unHijo)