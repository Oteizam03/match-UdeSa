#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:36:05 2026

@author: milagrosoteiza
"""

import pandas as pd
"""
df = pd.read_excel("C:/Users/justo/OneDrive/Documentos/programación/match-UdeSa/datos/dataframe.xlsx", dtype = {"id" : str, "sexo": str,
                                              "nombre": str, "apellido": str, "carrera": str, 
                                              "zona por la que vive": str, "hobbies": str,
                                              "estilo musical favorito": str, "edad" : int, "altura": int,
                                              "sexualidad": str, "instagram": str, "telefono": str}) #########
"""

#si no cambian esto, el codigo corre y sube el dataset para todos (soy uma)
url = "https://raw.githubusercontent.com/umapoggi/dataset/main/usuarios_50_udesa.xlsx"

df = pd.read_excel(url,dtype = {"id" : str, "sexo": str,
                                              "nombre": str, "apellido": str, "carrera": str, 
                                              "zona por la que vive": str, "hobbies": str,
                                              "estilo musical favorito": str, "edad" : int, "altura": int,
                                              "sexualidad": str, "instagram": str, "telefono": str})

from src.filtrado import filtrar_usuarios


def pedir_preferencias(edad_minima,edad_maxima, carrera_de_preferencia, altura_minima, altura_maxima, hobbie_de_interes, zona_de_interes, estilo_musical_de_preferencia):

  if edad_minima < 17 or edad_maxima > 30:
    raise ValueError ("edad no disponible para ser alumno de UdeSa")
  if carrera_de_preferencia not in df["carrera"]: #ver aca si es .values
    raise ValueError("ERROR, esa carrera no es de UdeSa, anda a buscar el amor en otro lado")
  if altura_minima < 100 or altura_maxima > 230:
    raise ValueError ("ERROR, altura no valida")
  if hobbie_de_interes not in df["hobbies"]: #ver aca si es .values
    raise ValueError("ERROR, ese hobbie no esta en la lista de opciones")
  if zona_de_interes not in df["zona por la que vive"]:       #ver aca si es .values
    raise ValueError("ERROR, zona no disponible entre las opciones que te di")
  if estilo_musical_de_preferencia not in df["estilo musical favorito"]:    #ver aca si es .values
    raise ValueError("ERROR,el estilo musical no esta dentro de las opciones")



try:
  id_usuario = input("ingrese el numero de id/legajo, son 5 numeros: ") #en funcion 1
  #llamado de funcion para validarla
  pedir_usuario(df, id_usuario) #############
  
  
  edad_minima = int(input("ingrese la edad minima con la que estas dispuesto a salir: ")) #en funcion 2
  edad_maxima = int(input("ingrese la edad maxima con la que estas dispuesto a salir: "))
  carrera_de_preferencia = input("ingrese la carrera que te gustaria que estudie el otro: ")
  altura_minima = int(input("ingrese la altura minima con el que estes dispuesto a salir: "))
  altura_maxima = int(input("ingrese la altura maxima con el que estes dispuesto a salir: "))
  hobbie_de_interes = input("ingrese UN hobbie que prefieras que haga el otro(lectura, gaming, musica, arte, deporte): ")
  zona_de_interes = input("ingrese la zona en la que preferis que viva el otro (norte/centro/sur): ")
  estilo_musical_de_preferencia = input("ingrese el estilo musical que preferis del otro (pop/reggaeton/rock/cumbia/clasica): ")
  
  #llamado de funcion para validarla
  pedir_preferencias(edad_minima,  edad_maxima, carrera_de_preferencia, altura_minima, altura_maxima,  hobbie_de_interes, zona_de_interes, estilo_musical_de_preferencia) #######
  
#hola chicos, soy Mili, agrego un par de cosas, si creen que esta mal las pueden borrar (les puse ####### al final para que reconozcan lo nuevo)


  fila = df[df["id"] == (id_usuario)] ###########
  nombre = fila["nombre"].values[0] ########
  apellido = fila["apellido"].values[0]  ###########
  print("Bienvenido", nombre, apellido, "esperemos que encuentres el amor y seas feliz") ###########
      
    
except ValueError as e: ###########
    print(e) ###########
    
else:
    print("los datos fueron cargados correctamente") ###########
    
#aca podria algo que llame a una funcion en otro archivo, que tenga el filtrado y el match llamando a otros archivos    
  
fila = df[df["id"] == id_usuario].iloc[0]
genero = fila["sexo"]
sexualidad = fila["sexualidad"]
print(filtrar_usuarios(df,genero, sexualidad, edad_minima, edad_maxima, altura_minima, id_usuario))  
    
    
    
#from src.calculo_match import obtener_match
#le pasamos la imformacion filtrada para hacer el calculo del match
#lista

#le pasamos los candidatos filtrados
#candidatos = filtrar_usuarios(df, genero, sexualidad, edad_min, edad_max, altura_min, id_usuario)  
"""preferencias = {
    "carrera_de_preferencia": carrera_de_preferencia,
    "zona_de_interes": zona_de_interes,
    "estilo_musical_de_preferencia": estilo_musical_de_preferencia,
    "hobbie_de_interes": hobbie_de_interes,
    "altura_minima": altura_minima,
    "altura_maxima": altura_maxima,
    "edad_minima": edad_minima,
    "edad_maxima": edad_maxima
}
"""
#match = obtener_match(df,id_usuario,candidatos, preferencias)
    
    
    
    
    
    
    
    
    
    
    
    
    
    