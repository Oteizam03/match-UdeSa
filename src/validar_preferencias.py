import pandas as pd

def validar_edad(edad): 
    if not edad.strip().isdigit(): 
        raise ValueError("ERROR, la edad tiene que ser un número entero no negativo")
    edad= int(edad)
    if edad < 17 or edad> 30:
      raise ValueError ("ERROR, edad no disponible dentro de los alumnos de UdeSa. Vuelva a ingresarla")
    return edad  

def validar_rango(rango1, rango2, preferencia): 
    if rango1 > rango2:
        raise ValueError (f"ERROR, la {preferencia} minima no puede ser mayor a la {preferencia} maxima")

def validar_altura(altura): 
    if not altura.strip().isdigit(): 
        raise ValueError("ERROR, la altura tiene que ser un número entero no negativo. Vuelva a ingresarla")
    altura=int(altura)
    if altura < 100 or altura > 230:
      raise ValueError ("ERROR, altura no valida, debe estar entre 100cm a 230cm. Vuelva a ingresarla")
    return altura

def validar_carrera(df, carrera): #esto en realidad podria no tenerlo y que validar carrera lo haga con de de validar_opcion
    if carrera not in df["carrera"].values:
      raise ValueError("ERROR, esa carrera no es de UdeSa o la escribiste mal. Escribila tal cual esta en la lista")
    return carrera

def validar_opcion(df, dato, columna, categoria): 
    dato = dato.strip().lower()
    if dato not in df[columna].str.lower().values: 
      raise ValueError(f"ERROR, el/la {categoria} ingresado/a no esta en la lista de opciones. ")  
    return dato

def pedir_con_validacion(prompt, funcion_que_lo_valida): 
    while True: 
        dato = input(prompt)
        try: 
            return funcion_que_lo_valida(dato)
            break
        except ValueError as e: 
            print(e)
def pedir_con_validacion2(df, prompt, funcion_que_valida, columna, categoria): 
    while True: 
        dato = input(prompt)
        try: 
            return funcion_que_valida(df, dato, columna, categoria)
            break
        except ValueError as e: 
            print(e)