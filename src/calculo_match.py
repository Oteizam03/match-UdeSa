#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 14:19:11 2026

@author: milagrosoteiza
"""
#partiendo de el dataset diltrado, vamos a calcular el porcentaje de match <3

def calculo_match(usuario, candidatos, preferencias):
    puntaje_de_amor = 50
    puntaje_categoria = 50/4
#chequear que hay que comparar: carrera, zona, hobbie, estilo de musica, edad, altura
    if candidatos["carrera"] == preferencias["carrera_de_preferencia"]:
        puntaje_de_amor += puntaje_categoria
    if candidatos["zona por la que vive"] == preferencias["zona_de_interes"]:
        puntaje_de_amor += puntaje_categoria
    if candidatos["hobbies"] == preferencias["hobbie_de_interes"]:
        puntaje_de_amor += puntaje_categoria
    if candidatos["estilo musical favorito"] == preferencias["estilo_musical_de_preferencia"]:
        puntaje_de_amor += puntaje_categoria
        
    return puntaje_de_amor
    

def obtener_match(df,id_usuario,candidatos, preferencias):
    usuario = df[df["id"]== id_usuario]#traigo la ifnormacion del usuario, busca en le dataframe que el id coincida con el id usuairo
    futuros_amores = []# lista vacia dondo voy a ir agregando a mis amores posibles
    for i,candidato in candidatos.iterrows(): #i me da el numero de la fila, candidato me da el dato de esa fila (dicc)
                                            #iterrows() es una funcion que permite recorrer un dataframe fila por fila
        puntaje_compatible = calculo_match(usuario, candidato, preferencias)
        if puntaje_compatible > 50:
            
            futuros_amores.append({
                "id": candidato["id"],
                "puntaje": puntaje_compatible,
                "nombre": candidato["nombre"],
                "apellido": candidato["apellido"],
                "instagram": candidato["instagram"],
                "telefono": candidato["telefono"]
            })
    
    return futuros_amores
    
    
    
    
    


    