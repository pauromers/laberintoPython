#!/usr/bin/python
#-*- coding: utf-8 -*-

class ElementoMapa:
    def __init__(self):
        self.padre=None

    def entrar(self):
        raise NotImplementedError("Subclase debe implementar este metodo.")
