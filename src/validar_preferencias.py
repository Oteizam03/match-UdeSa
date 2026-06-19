import pandas as pd

def validar_edad(edad): 
    """
    Valida que la edad sea un entero dentro del rango de 17 a 30 años.

    Parameters
    ----------
    edad : str
        Edad ingresada por el usuario como texto.

    Returns
    -------
    int
        La edad convertida a entero si es válida.

    Raises
    ------
    ValueError
        Si no es un número entero no negativo, o si está fuera del rango 17–30.
    """
    if not edad.strip().isdigit(): 
        raise ValueError("ERROR, la edad tiene que ser un número entero no negativo")
    edad= int(edad)
    if edad < 17 or edad> 30:
      raise ValueError ("\nERROR, edad no disponible dentro de los alumnos de UdeSa. Vuelva a ingresarla")
    return edad  

def validar_rango(rango1, rango2, preferencia): 
    """
    Valida que el extremo mínimo de un rango no supere al máximo.

    Parameters
    ----------
    rango1 : int
        Valor mínimo del rango.
    rango2 : int
        Valor máximo del rango.
    preferencia : str
        Nombre de la preferencia, usado en el mensaje de error
            (ej. "edad", "altura").

    Returns
    -------
    None

    Raises
    ------
    ValueError
        Si rango1 es mayor que rango2.
    """
    if rango1 > rango2:
        raise ValueError (f"\nERROR, la {preferencia} minima no puede ser mayor a la {preferencia} maxima")

def validar_altura(altura): 
    """
    Valida que la altura sea un entero dentro del rango permitido (en cm).

    Parameters
    ----------
    altura : str
       Altura ingresada por el usuario como texto.

    Returns
    -------
    int
        La altura convertida a entero si es válida..

    Raises
    ------
    ValueError
        Si no es un número entero no negativo, o si está
            fuera del rango 100–230 cm.
    """
    if not altura.strip().isdigit(): 
        raise ValueError("\nERROR, la altura tiene que ser un número entero no negativo. Vuelva a ingresarla")
    altura=int(altura)
    if altura < 100 or altura > 230:
      raise ValueError ("\nERROR, altura no valida, debe estar entre 100cm a 230cm. Vuelva a ingresarla")
    return altura

def validar_carrera(df, carrera): 
    """
    Valida que la carrera ingresada exista en el DataFrame.

    Parameters
    ----------
    df : DataFrame
        DataFrame con la columna "carrera".
    carrera : str
        Carrera ingresada por el usuario.

    Returns
    -------
    str
        La carrera si está presente en el DataFrame.

    Raises
    ------
    ValueError
        Si la carrera no figura en la columna "carrera".
    """
    if carrera not in df["carrera"].values:
      raise ValueError("\nERROR, esa carrera no es de UdeSa o la escribiste mal. Escribila tal cual esta en la lista")
    return carrera

def validar_opcion(df, dato, columna, categoria): 
    """
    Valida que un dato exista en una columna del DataFrame (sin distinguir mayúsculas).
    Normaliza el dato (strip + minúsculas) y lo compara contra los valores
    de la columna también en minúsculas.

    Parameters
    ----------
    df : DataFrame
        DataFrame donde se busca el dato.
    dato : str
        Valor ingresado por el usuario.
    columna : str
        Nombre de la columna donde se valida.
    categoria : str
        ombre de la categoría, usado en el mensaje de error.

    Returns
    -------
    str
        El dato normalizado (sin espacios y en minúsculas) si es válido.

    Raises
    ------
    ValueError
        Si el dato no está entre las opciones de la columna.
    """
    dato = dato.strip().lower()
    if dato not in df[columna].str.lower().values: 
      raise ValueError(f"\nERROR, el/la {categoria} ingresado/a no esta en la lista de opciones. ")  
    return dato

def pedir_con_validacion(prompt, funcion_que_lo_valida): 
    """
    Pide un dato por consola y lo revalida hasta que sea válido.
    Repite el input hasta que la función de validación no lance ValueError.

    Parameters
    ----------
    prompt : str
       Mensaje que se muestra al pedir el dato.
    funcion_que_lo_valida : 
        Función que valida el dato y lo devuelve, o lanza ValueError si es inválido.

    Returns
    -------
        El dato ya validado que devuelve funcion_que_lo_valida..
    """
    while True: 
        dato = input(prompt)
        try: 
            return funcion_que_lo_valida(dato)
            
        except ValueError as e: 
            print(e)
def pedir_con_validacion2(df, prompt, funcion_que_valida, columna, categoria): 
    """
    Pide un dato por consola y lo revalida contra un DataFrame hasta que sea válido.

    Parameters
    ----------
    df : DataFrame
        DataFrame que se pasa a la función de validación.
    prompt : str
        Mensaje que se muestra al pedir el dato.
    funcion_que_valida : TYPE
        Función que valida el dato contra el df.
    columna : str
        Nombre de la columna donde se valida.
    categoria : str
        Nombre de la categoría, usado en el mensaje de error.

    Returns
    -------
        El dato ya validado que devuelve funcion_que_valida.
    """
    while True: 
        dato = input(prompt)
        try: 
            return funcion_que_valida(df, dato, columna, categoria)
        
        except ValueError as e: 
            print(e)
            