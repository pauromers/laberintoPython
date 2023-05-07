#!/usr/bin/python
#-*- coding: utf-8 -*-

class Laberinto:
 
    def __init__(self):
        self.habitaciones = []
    
    def get_habitaciones(self):
        return self.habitaciones

    def agregarHabitacion(self, unaHab):
        self.habitaciones.append(unaHab)

    
