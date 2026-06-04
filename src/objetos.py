import pandas as pd

class Usuario:
    def __init__(self, legajo, nombre, sexualidad, carrera, altura, edad, pref_carreras, pref_altura_min, pref_altura_max, pref_edad_min, pref_edad_max):
        
        self.legajo = legajo
        self.nombre = nombre
        self.carrera = carrera
        self.altura = altura
        self.edad = edad
        self.sexualidad = sexualidad
        
        self.pref_carreras = pref_carreras
        self.pref_altura_min = pref_altura_min
        self.pref_altura_max = pref_altura_max
        self.pref_edad_min = pref_edad_min
        self.pref_edad_max = pref_edad_max
        
        #metodos
        #metodo: 
            
            
            
            
            
            
            
            
chicos ahi arme la parte de sexualidad, despues hay que ubicarla bien 

 # HETEROSEXUAL
 
dedf calcular_compatibilidad_sexual (dentro de un metodo)
    if self.sexualidad == "heterosexual":

        if self.sexo == "F":
            return otro.sexo == "M"

        if self.sexo == "M":
            return otro.sexo == "F"

    # HOMOSEXUAL
    elif self.sexualidad == "homosexual":

        if self.sexo == "F":
            return otro.sexo == "F"

        if self.sexo == "M":
            return otro.sexo == "M"

    # BISEXUAL
    elif self.sexualidad == "bisexual":
        return otro.sexo in ["M", "F"]

    return False