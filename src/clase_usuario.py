#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Usuario:
    def __init__(self, legajo, nombre, carrera, altura, edad, pref_carreras, pref_altura_min, pref_altura_max, pref_edad_min, pref_edad_max):
        
        self.legajo = legajo
        self.nombre = nombre
        self.carrera = carrera
        self.altura = altura
        self.edad = edad
        
        self.pref_carreras = pref_carreras
        self.pref_altura_min = pref_altura_min
        self.pref_altura_max = pref_altura_max
        self.pref_edad_min = pref_edad_min
        self.pref_edad_max = pref_edad_max
        