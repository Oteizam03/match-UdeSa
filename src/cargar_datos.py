import pandas as pd
import os

def cargar_datos(ruta):
    '''
    Carga un archivo CSV y lo retorna como un DataFrame de pandas
   
    Parameters:
        ruta (str): ruta al archivo CSV con los datos sobre los cuales se van a calcular las mediciones en posteriores funciones.
        
    Return:
        DataFrame: DataFrame con columnas "id": str, "sexo": str,
                    "nombre": str, "apellido": str, "carrera": str,
                    "zona por la que vive": str, "hobbies": str,
                    "estilo musical favorito": str, "edad": int, "altura": int,
                    "sexualidad": str, "instagram": str, "telefono": str
    Raises:
        FileNotFoundError: Si el archivo no existe en la ruta indicada
    '''
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"no se encontro el archivo en la ruta {ruta}")
        
    df = pd.read_excel(ruta, dtype ={
        "id": str, "sexo": str,
        "nombre": str, "apellido": str, "carrera": str,
        "zona por la que vive": str, "hobbies": str,
        "estilo musical favorito": str, "edad": int, "altura": int,
        "sexualidad": str, "instagram": str, "telefono": str
        })
    return df
