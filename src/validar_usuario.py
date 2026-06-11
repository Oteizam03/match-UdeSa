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
    Valida que el ID ingresado corresponda a un alumno registrado en la base de datos.

    La función verifica que el ID tenga exactamente 5 caracteres y que exista
    dentro de la columna "id" del DataFrame recibido. Si alguna de estas
    condiciones no se cumple, se lanza un ValueError. La función no muestra
    mensajes por pantalla; el manejo del error debe hacerse desde el programa
    principal, por ejemplo mediante un bloque try/except.

    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame que contiene la información de los alumnos de grado de la
        Universidad de San Andrés. Debe incluir una columna llamada "id".

    id_usuario : str
        Identificador del alumno ingresado por el usuario. Debe tener
        exactamente 5 caracteres.

    Raises
    ------
    ValueError
        Si el ID ingresado no tiene exactamente 5 caracteres.

    ValueError
        Si el ID ingresado no se encuentra en la columna "id" del DataFrame.

    Returns
    -------
    None
        La función no retorna ningún valor. Solo valida el usuario o lanza un
        error si la validación falla.
    """
    if len(id_usuario)!= 5:
        raise ValueError ("error, el numero de usuario no cumple con las caracteristicas solicitadas")
    if id_usuario not in df["id"].values:
        raise ValueError("Error, tu id no esta en nuestra base de datos, no sos alumno de UdeSa")
        
    

        
        
    
