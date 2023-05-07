#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Contenedor(ElementoMapa):
    def __init__(self):
        self.hijos = []

    def agregarHijo(self,unEM: ElementoMapa):
        unEM.padre = self  # El padre es el contenedor
        self.hijos.append(unEM)


