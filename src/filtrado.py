import pandas as pd 


def filtrar_usuarios(df,genero, sexualidad, edad_min, edad_max, altura_min, id_usuario): 
    """
            Filtra el DataFrame eliminando perfiles incompatibles con el usuario.
            
            parametros:
                df (DataFrame): dataset completo de usuarios 
                genero (str): sexo del usuario ("m" o "f")
                sexualidad (str): orientacion del usuario ("heterosexual", "homosexual", "bisexual")
                edad_min (int): edad mínima aceptada para el match (aclarado por el usuario)
                edad_max(int): edad máxima aceptada para el match
                altura_min(int): altura maxima aceptada para el match (en cm)
                id_usuario (str): legajo del usuario activo, para excluirse a sí mismo
                
            returns:
                candidatos (dataframe): subconjunto de candidatos que pasan los filtros duros
    """
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
        candidatos = candidatos[(((candidatos["sexualidad"] == "homosexual") | (candidatos["sexualidad"] == "bisexual")) & (candidatos["sexo"] == genero)) | (((candidatos["sexualidad"] == "heterosexual") | (candidatos["sexualidad"] == "bisexual")) & (candidatos["sexo"] != genero))]
        
        
    
    return candidatos
