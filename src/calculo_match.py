#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 14:19:11 2026

@author: milagrosoteiza
"""
#partiendo de el dataset diltrado, vamos a calcular el porcentaje de match <3




def calculo_match(usuario, candidatos, preferencias):
    """
    Esta funcion compara al candidato con las preferencias del usuario y calcula el porcentaje de compatibilidad. 
    Todos los candidatos empiezan con un porcentaje de 50%, ya que pasaron el filtrar_usuario.
    Parametros: 
        usuario (dataframe): es el usuario al que le estoy buscando su match.
        candidatos (dataframe): son los datos del candidato a comparar/evaluar.
        preferencias (diccionario) : contiene las preferencias del usuario.
    
    Returns (str): devuelve el porcentaje de compatibilidad. 

    """
    puntaje_de_amor = 50
    puntaje_categoria = 12.5
#chequear que hay que comparar: carrera, zona, hobbie, estilo de musica, edad, altura
    if candidatos["carrera"].lower() == preferencias["carrera_de_preferencia"]:
        puntaje_de_amor += puntaje_categoria
    if candidatos["zona por la que vive"].lower() == preferencias["zona_de_interes"]:
        puntaje_de_amor += puntaje_categoria
    if candidatos["hobbies"].lower() == preferencias["hobbie_de_interes"]:
        puntaje_de_amor += puntaje_categoria
    if candidatos["estilo musical favorito"].lower() == preferencias["estilo_musical_de_preferencia"]:
        puntaje_de_amor += puntaje_categoria
        
    return f"{round(puntaje_de_amor)}%"
    

def obtener_match(df,id_usuario,candidatos, preferencias):
    """
    Esta funcion recorre los candidatos filtrados, calcula el porcentaje de compatibilidad y los agrupa en una lista. 
    Parameters:
        df (dataframe): son todos los datos del usuario.
        id_usuario (str) : es el legajo del usuario.
        candidatos (dataframe): subconjunto de candidatos que pasan los filtros.
        preferencias(diccionario) : contiene las preferencias del usuario.
       
    Returns (list): me devuelve una lista de diccionarios con toda la informacion de todos los posibles matches.

    """
    usuario = df[df["id"]== id_usuario]#traigo la ifnormacion del usuario, busca en le dataframe que el id coincida con el id usuairo
    futuros_amores = []# lista vacia dondo voy a ir agregando a mis amores posibles
    for i,candidato in candidatos.iterrows(): #i me da el numero de la fila, candidato me da el dato de esa fila (dicc)
                                            #iterrows() es una funcion que permite recorrer un dataframe fila por fila
        puntaje_compatible = calculo_match(usuario, candidato, preferencias)
        

        futuros_amores.append({
            "id": candidato["id"],
            "puntaje": puntaje_compatible, #devuelve un str
            "nombre": candidato["nombre"],
            "apellido": candidato["apellido"],
            "instagram": candidato["instagram"],
            "telefono": candidato["telefono"],
            "zona por la que vive": candidato["zona por la que vive"]
        })
    
    return futuros_amores
    


    
    
    
    


    