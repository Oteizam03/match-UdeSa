#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:20:46 2026

@author: milagrosoteiza
"""

import pandas as pd

def validar_usuario(df, id_usuario):
  if len(id_usuario)!= 5:
    raise ValueError ("error, el numero de usuario no cumple con las caracteristicas solicitadas")
  if id_usuario not in df["id"]: #ver aca si es .values
    raise ValueError("Error, tu id no esta en nuestra base de datos, no sos alumno de UdeSa")
    
