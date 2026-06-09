import pandas as pd 
"""
df = pd.read_excel("dataframe.xlsx", dtype = {"id" : str, "sexo": str,
                                              "nombre": str, "apellido": str, "carrera": str, 
                                              "zona por la que vive": str, "hobbies": str,
                                              "estilo musical favorito": str, "edad" : int, "altura": int,
                                              "sexualidad": str, "instagram": str, "telefono": str})
"""

def filtrar_usuarios(df,genero, sexualidad, edad_min, edad_max, altura_min, id_usuario): 
    
    candidatos = df[df["id"] != id_usuario].copy()# esto fue con chat

    candidatos = candidatos[
        (candidatos["edad"] >= edad_min) &
        (candidatos["edad"] <= edad_max) &
        (candidatos["altura"] >= altura_min) 
    ]
                
    if sexualidad == "homosexual": 
        candidatos = candidatos[((candidatos["sexualidad"] == "homosexual") | (candidatos["sexualidad"] == "bisexual")) & (candidatos["sexo"] == genero)]
    elif sexualidad == "heterosexual":
        candidatos = candidatos[((candidatos["sexualidad"] == "heterosexual") | (candidatos["sexualidad"] == "bisexual")) & (candidatos["sexo"] != genero)]
    else:
        candidatos = candidatos[((candidatos["sexualidad"] == "heterosexual") & (candidatos["sexo"] != genero)) | (candidatos["sexualidad"] == "bisexual") | ((candidatos["sexualidad"] == "homosexual") & (candidatos["sexo"] == genero))]
        
        
    
    return candidatos
