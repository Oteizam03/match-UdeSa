#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:45:40 2026

@author: milagrosoteiza
"""
from src.validar_preferencias import pedir_con_validacion, validar_altura, validar_rango, validar_edad, pedir_con_validacion2, validar_opcion, validar_carrera


def pedir_preferencias(df): 
    """ 
    Solicita y valida las preferencias del usuario para buscar posibles matches.
    La función pide por consola distintos criterios de preferencia del usuario: edad mínima y máxima, altura mínima y máxima, 
    hobbie, estilo musical, zona de residencia y carrera de preferencia. 
    
    Cada dato ingresado se valida utilizando funciones auxiliares del módulo validar_preferencias. 
    Para validar hobbie, estilo musical, zona y carrera, la función compara los datos ingresados con las opciones disponibles en el DataFrame recibido como parámetro.
    
    Parámetros 
    ----------
    df : pandas.DataFrame
        DataFrame con la información de los alumnos. Debe contener, al menos, las columnas "carrera", "hobbies", "estilo musical favorito" y "zona por la que vive",
        ya que estas se usan para validar las preferencias. 
    
    Returns
    ------- 
    tuple Tupla con las preferencias validadas del usuario, en el siguiente orden:
        edad_min : int Edad mínima con la que el usuario estaría dispuesto a salir.
        
        edad_max : int Edad máxima con la que el usuario estaría dispuesto a salir. 
        
        altura_min : int Altura mínima, en centímetros, con la que el usuario estaría dispuesto a salir. 
        
        altura_max : int Altura máxima, en centímetros, con la que el usuario estaría dispuesto a salir. 
        
        hobbie : str Hobbie que el usuario prefiere que tenga la otra persona. 
        
        musica : str Estilo musical que el usuario prefiere que le guste a la otra persona. 
        
        zona_donde_vive : str Zona en la que el usuario prefiere que viva la otra persona. 
        
        carrera : str Carrera que el usuario prefiere que estudie la otra persona.
        """
    print("Bienvenido a MATCH UDESA, esperemos que encuentre el amor, sea paciente. A continuacion le solicitaremos sus preferencias con respecto al otro para asi relacionarlo con posibles matches")
    
    altura_min = pedir_con_validacion("ingrese la altura minima con el que estes dispuesto a salir en cm (ej: 155): ", validar_altura)
    while True: 
        altura_max = pedir_con_validacion("ingrese la altura maxima con el que estes dispuesto a salir en cm (ej: 175): ", validar_altura)
        try: 
            validar_rango(altura_min, altura_max, "altura")
            break
        except ValueError as e: 
            print (e)
    
    edad_min =  pedir_con_validacion("ingrese la edad minima con la que estas dispuesto a salir: ", validar_edad)
    while True:
        edad_max = pedir_con_validacion("ingrese la edad maxima con la que estas dispuesto a salir: ", validar_edad)
        try: 
            validar_rango(edad_min, edad_max, "edad")
            break
        except ValueError as e:
            print (e)
    print("Sabemos que pedimos muchos datos, SE PACIENTE, es para encntrar a tu AMOR PERFECTO")
    hobbie = pedir_con_validacion2(df, "ingrese UN hobbie que prefieras que haga el otro(lectura, gaming, musica, arte, deporte): ", validar_opcion, "hobbies", "hobbie")
    musica = pedir_con_validacion2(df, "ingrese el estilo musical que preferis del otro (pop/reggaeton/rock/cumbia/clasica): ", validar_opcion, "estilo musical favorito", "estilo de musica") 
    zona_donde_vive = pedir_con_validacion2(df, "ingrese la zona en la que preferis que viva el otro (norte/centro/sur): ", validar_opcion, "zona por la que vive", "zona")
    while True: 
        carrera = input("ingrese la carrera que te gustaria que estudie el otro, puede COPIAR Y PEGAR de la siguiente lista --------------------------------------- "                              
                        
        "(abogacia, administracion de empresas, ciencia politica y gobierno, ciencias de la educacion, "
        "ciencias del comportamiento, comunicacion, contador publico, diseno, economia, economia empresarial, "
        "finanzas, humanidades, ingenieria en biotecnologia, ingenieria en inteligencia artificial, "
        "ingenieria en sustentabilidad, negocios digitales, profesorado en educacion primaria, "
        "relaciones internacionales): ")
        try: 
            validar_carrera(df, carrera)
            break
        except ValueError as e: 
            print(e)

    return (edad_min, edad_max, altura_min, altura_max, hobbie, musica, zona_donde_vive, carrera)











