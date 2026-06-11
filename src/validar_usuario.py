#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:20:46 2026

@author: milagrosoteiza
"""
from src.cargar_datos import cargar_datos
import pandas as pd

def validar_usuario(df, id_usuario):
    """

    Esta funcion se encarga de validar el usuario de udesa ingresado por el usuario de Match UdeSA
    
    
    df : DataFrame
        contiene las caracteristicas de los alumnos de grado se la universidad de San Andres. Tiene 13 columnas y el dataframe creado tiene 1500 filas. Pero se pueden agregar filas sin problema. 
    id_usuario : str
        son los 5 numeros que identifican al alumno.

    Raises
    ------
    ValueError
        si no cumple con la longitud de cinco numeros
    ValueError
          si no esta el id en la base de datos de UdeSa

    Returns
    -------
    None.

    """
    if len(id_usuario)!= 5:
        raise ValueError ("error, el numero de usuario no cumple con las caracteristicas solicitadas")
    if id_usuario not in df["id"].values:
        raise ValueError("Error, tu id no esta en nuestra base de datos, no sos alumno de UdeSa")
        
    

        
        
    
