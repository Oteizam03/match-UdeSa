import pandas as pd

def validar_preferencias(df, altura_min, altura_max, edad_max, edad_min, hobbie, carrera, estilo_musical, zona_donde_vive): 

    '''
    Verifica que las preferencias ingresadas por el usuario sean validas. /
    Si no lo son levanta un error con un mensaje especificando que sucedio. 
    
    Parametros: 
        df: DataFrame 
        Es un dataframe con todos los datos de los alumnos de UdeSa
        
        altura_min: int
        Numero que representa la altura minima que el match del usuario puede tener en cm. Debe ser >= 100.
        
        altura_max: int 
        Numero que representa la altura maxima que el match del usuario puede tener en cm. Debe ser <= 230.
        
        edad_max: int
        Numero que representa la edad maxima que el match del usuario puede tener. Debe ser <= 30.
        
        edad_min: int
        Numero que representa la edad minima que el mach del usuario puede tener. Debe ser >= 17
        
        hobbie: str
        Hobbie que el usuario prefiere que su match realice. Debe estar en la lista de hobbies disponibles
        
        carrera: str 
        Carrera de grado que el usuario prefiere que su match estudie. Debe estar entre las opciones disponibles.
        
        estilo_musical: str 
        Estilo musical que el usuario prefiere que su match escuche. Debe estar entre los estilos disponibles.
        
        zona_donde_vive: str 
        Zona en donde el usuario prefiere que viva su match. Debe estar entre las opciones disponibles. 
    
    Raises: 
        ValueError: 
            Si alguno de los parametros no cumple con las validaciones correspondientes.
    '''
    if altura_min < 100 or altura_max > 230:
      raise ValueError ("ERROR, altura no valida, debe estar entre 100cm a 230cm")
    if edad_min < 17 or edad_max > 30:
      raise ValueError ("edad no disponible dentro de los alumnos de UdeSa")
    if edad_min> edad_max: 
        raise ValueError("ERROR, la edad minima no puede ser mayor a la edad maxima")
    if hobbie not in df["hobbies"].values: 
      raise ValueError("ERROR, ese hobbie no esta en la lista de opciones")  
    if carrera not in df["carrera"].values:
      raise ValueError("ERROR, esa carrera no es de UdeSa, anda a buscar el amor en otro lado")
    if estilo_musical not in df["estilo musical favorito"].values:   
      raise ValueError("ERROR, el estilo musical no esta dentro de las opciones")
    if zona_donde_vive not in df["zona por la que vive"].values:      
      raise ValueError("ERROR, zona no disponible entre las opciones que te di")
    

