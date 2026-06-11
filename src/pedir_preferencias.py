#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:45:40 2026

@author: milagrosoteiza
"""
def pedir_preferencias():
    """
    esta funcion le solicita al usuario sus preferencias en terinos amorosos. Es decir, que busca el usuario en el otro. El objetivo es juntar esta informacion para luego comparar posibles matches

    parametros
     None
     
    Returns
    -------
    altura_minima : str
        es la altura minima con la que el usuario saldria
    altura_maxima : str
        es la altura maxima con la que el usuario estaria
    edad_maxima : str
        es la edad maxima con la que el usuario esta duspuesto a salir
    edad_minima : str
        es la edad minima con la que el usuario esta duspuesto a salir
    hobbie_de_interes : str
        es el hobbie que el usuario busca que haga el otro
    carrera_de_preferencia : str
        es la carera que el usuario busca que haga el otro
    estilo_musical_de_preferencia : str
        es el estilo musical que busca que le guste al otro
    zona_de_interes : str
        la zona por donde quiere que viva el otro.

    """
    
    edad_minima = input("ingrese la edad minima con la que estas dispuesto a salir: ")
    edad_maxima = input("ingrese la edad maxima con la que estas dispuesto a salir: ")
    carrera_de_preferencia = input("ingrese la carrera que te gustaria que estudie el otro: ")
    altura_minima = input("ingrese la altura minima con el que estes dispuesto a salir en cm (ej: 155): ")
    altura_maxima = input("ingrese la altura maxima con el que estes dispuesto a salir en cm (ej: 175): ")
    hobbie_de_interes = input("ingrese UN hobbie que prefieras que haga el otro(lectura, gaming, musica, arte, deporte): ")
    zona_de_interes = input("ingrese la zona en la que preferis que viva el otro (norte/centro/sur): ")
    estilo_musical_de_preferencia = input("ingrese el estilo musical que preferis del otro (pop/reggaeton/rock/cumbia/clasica): ")
    
    return (altura_minima, altura_maxima, edad_maxima, edad_minima, hobbie_de_interes, carrera_de_preferencia, estilo_musical_de_preferencia, zona_de_interes)