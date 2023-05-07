#!/usr/bin/python
#-*- coding: utf-8 -*-

from Baul import Baul
from Bomba import Bomba
from Habitacion import Habitacion
from Puerta import Puerta
from Pared import Pared
from Laberinto import Laberinto
from Espada import Espada
from Contenedor import Contenedor
from Bicho import Bicho

class Juego:
    
    def __init__ (self):
        self.laberinto=None
        self.bichos = []
        
    def fabricarLaberinto(self):
        laberinto = Laberinto()
        return laberinto
    
    def fabricarHabitacion(self, unNum):
        hab = Habitacion(unNum)
        return hab

    def fabricarPuertaLado1Lado2(self, abierta, unaHab, otraHab):
        puerta = Puerta(abierta, unaHab, otraHab)
        return puerta

    def fabricarPared(self):
        return Pared()
    
    def fabricarBaulEn(self, cont: Contenedor):
        unNum = len(cont.hijos)
        baul=Baul(unNum)
        cont.agregarHijo(baul)

    def fabricarEspadaEn(self,cont: Contenedor):
        espada = Espada()
        cont.agregarHijo(espada)

    def fabricarBombaEn(self,cont: Contenedor):
        bomba = Bomba()
        cont.agregarHijo(bomba)

    def laberinto2HabitacionesFM(self):
        self.laberinto = self.fabricarLaberinto()

        abierta=True
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)

        puerta = self.fabricarPuertaLado1Lado2(abierta,hab1, hab2)
        hab1.sur = puerta
        hab2.norte = puerta
        
        hab1.norte = self.fabricarPared()
        hab1.oeste = self.fabricarPared()
        hab1.este = self.fabricarPared()
        
        hab2.sur = self.fabricarPared()
        hab2.oeste = self.fabricarPared()
        hab2.este = self.fabricarPared()
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

    def laberinto4Habitaciones2Ba(self):
        self.laberinto = self.fabricarLaberinto()
            
        abierta=True
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)

        puerta1 = self.fabricarPuertaLado1Lado2(abierta,hab1, hab2)
        hab1.este = puerta1
        hab2.oeste = puerta1
            
        hab1.norte = self.fabricarPared()
        hab1.oeste = self.fabricarPared()
            
        puerta2 = self.fabricarPuertaLado1Lado2(abierta,hab1, hab3)
        hab1.sur=puerta2
        hab3.norte=puerta2

        hab3.oeste=self.fabricarPared()
        hab3.sur=self.fabricarPared()

        puerta3 = self.fabricarPuertaLado1Lado2(abierta,hab3, hab4)
        hab3.este=puerta3
        hab4.oeste=puerta3
            
        hab4.sur = self.fabricarPared()
        hab4.este = self.fabricarPared()
        
        puerta4 = self.fabricarPuertaLado1Lado2(abierta,hab2, hab4)
        hab2.sur=puerta4
        hab4.norte=puerta4

        hab2.norte=self.fabricarPared()
        hab2.este=self.fabricarPared()

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

        baul1=self.fabricarBaulEn(hab2)
        self.fabricarBombaEn(baul1)

        baul2=self.fabricarBaulEn(hab3)
        self.fabricarEspadaEn(baul2)

    def obtenerhabitacion(self, un_num: int):
        return self.laberinto.get_habitaciones(un_num)
        
    def agregar_bicho(self, un_bicho: Bicho):
        hab = self.obtenerhabitacion(1)
        un_bicho.posicion = hab
        self.bichos.append(un_bicho)




    
