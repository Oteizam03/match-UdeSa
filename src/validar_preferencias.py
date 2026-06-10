def validar_preferencias(altura_min, altura_max, edad_max, edad_min, hobbie, carrera, estilo_musical, zona_donde_vive): 

    '''
    Verifica que las preferencias ingresadas por el usuario sean validas. /
    Si no lo son levanta un error con un mensaje especificando que sucedio. 
    
    Parametros: 
        altura_min: int
        Numero que representa la altura minima que el match del usuario puede tener en cm. Debe ser >= 130.
        
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
    
