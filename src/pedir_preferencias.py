#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:45:40 2026

@author: milagrosoteiza
"""
def pedir_preferencias():

    """
    Solicita al usuario sus preferencias para buscar posibles matches.

    La función pide por consola distintos criterios de preferencia del usuario,
    como edad mínima y máxima, carrera, altura mínima y máxima, hobbie, zona de
    residencia y estilo musical. 
    
    
    Estos datos luego pueden utilizarse para
    comparar las preferencias ingresadas con la información disponible en la
    base de datos de alumnos.

    Parámetros
    ----------
    None
        Esta función no recibe parámetros.

    Returns
    -------
    tuple
        Tupla con las preferencias ingresadas por el usuario, en el siguiente
        orden:

        altura_minima : str
            Altura mínima, en centímetros, con la que el usuario estaría
            dispuesto a salir.

        altura_maxima : str
            Altura máxima, en centímetros, con la que el usuario estaría
            dispuesto a salir.

        edad_maxima : str
            Edad máxima con la que el usuario estaría dispuesto a salir.

        edad_minima : str
            Edad mínima con la que el usuario estaría dispuesto a salir.

        hobbie_de_interes : str
            Hobbie que el usuario prefiere que tenga la otra persona.

        carrera_de_preferencia : str
            Carrera que el usuario prefiere que estudie la otra persona.

        estilo_musical_de_preferencia : str
            Estilo musical que el usuario prefiere que le guste a la otra
            persona.

        zona_de_interes : str
            Zona en la que el usuario prefiere que viva la otra persona.
    """
    
    edad_minima = input("ingrese la edad minima con la que estas dispuesto a salir: ")
    edad_maxima = input("ingrese la edad maxima con la que estas dispuesto a salir: ")    
    carrera_de_preferencia = input("ingrese la carrera que te gustaria que estudie el otro "
    "(abogacia, administracion de empresas, ciencia politica y gobierno, ciencias de la educacion, "
    "ciencias del comportamiento, comunicacion, contador publico, diseno, economia, economia empresarial, "
    "finanzas, humanidades, ingenieria en biotecnologia, ingenieria en inteligencia artificial, "
    "ingenieria en sustentabilidad, negocios digitales, profesorado en educacion primaria, "
    "relaciones internacionales): ")
    altura_minima = input("ingrese la altura minima con el que estes dispuesto a salir en cm (ej: 155): ")
    altura_maxima = input("ingrese la altura maxima con el que estes dispuesto a salir en cm (ej: 175): ")
    hobbie_de_interes = input("ingrese UN hobbie que prefieras que haga el otro(lectura, gaming, musica, arte, deporte): ")
    zona_de_interes = input("ingrese la zona en la que preferis que viva el otro (norte/centro/sur): ")
    estilo_musical_de_preferencia = input("ingrese el estilo musical que preferis del otro (pop/reggaeton/rock/cumbia/clasica): ")
    
    return (altura_minima, altura_maxima, edad_maxima, edad_minima, hobbie_de_interes, carrera_de_preferencia, estilo_musical_de_preferencia, zona_de_interes)












