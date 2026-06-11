import pandas as pd
#si no cambian esto, el codigo corre y sube el dataset para todos (soy uma)
url = "https://raw.githubusercontent.com/umapoggi/dataset/main/usuarios_50_udesa.xlsx"

df = pd.read_excel(url,dtype = {"id" : str, "sexo": str,
                                              "nombre": str, "apellido": str, "carrera": str, 
                                              "zona por la que vive": str, "hobbies": str,
                                              "estilo musical favorito": str, "edad" : int, "altura": int,
                                              "sexualidad": str, "instagram": str, "telefono": str})

from src.filtrado import filtrar_usuarios
from src.validar_preferencias import validar_preferencias
from src.calculo_match import calculo_match
from src.Graficos import grafico_match
from src.pedir_preferencias import pedir_preferencias
from src.pedir_usuario import validar_usuario


while True: #agrego un while para que si salta un error el usuario vuelva a cargar sus datos. Lo unico, vuelve a preguntar desde cero, si quisieramos que repregunte solo el dato en el que tuvo error habria que hacer un loop especifico para cada variable
    try:
      id_usuario = input("ingrese el numero de id/legajo, son 5 numeros: ") 
      validar_usuario(df, id_usuario) 
      
      (altura_minima, altura_maxima, edad_maxima, edad_minima, hobbie_de_interes, carrera_de_preferencia, estilo_musical_de_preferencia, zona_de_interes) = pedir_preferencias()
      #aca en realidad habria que asignar las variables con un = y desp llamar a la funcion. pedir_preferencias(edad_minima,  edad_maxima, carrera_de_preferencia, altura_minima, altura_maxima,  hobbie_de_interes, zona_de_interes, estilo_musical_de_preferencia) #######
      validar_preferencias(df, altura_minima, altura_maxima, edad_maxima, edad_minima, hobbie_de_interes, carrera_de_preferencia, estilo_musical_de_preferencia, zona_de_interes)
      
      #esto podria ser una funcion
      fila = df[df["id"] == (id_usuario)] 
      nombre = fila["nombre"].values[0]
      apellido = fila["apellido"].values[0]
      print("Bienvenido", nombre, apellido, "esperemos que encuentres el amor y seas feliz") 
          
        
    except ValueError as e:
        print(e) 
        print("Por favor vuelva a ingresar los datos otra vez")
    
    else:
        print("los datos fueron cargados correctamente") 
        break
    
#esto deberia estar en filtrar usuarios 
fila = df[df["id"] == id_usuario].iloc[0]
genero = fila["sexo"]
sexualidad = fila["sexualidad"]
print(filtrar_usuarios(df,genero, sexualidad, edad_minima, edad_maxima, altura_minima, id_usuario))  

matches = calculo_match()
mensaje = grafico_match(matches)
print(mensaje)
    
    
#from src.calculo_match import obtener_match
#le pasamos la imformacion filtrada para hacer el calculo del match
#lista

#le pasamos los candidatos filtrados
#candidatos = filtrar_usuarios(df, genero, sexualidad, edad_min, edad_max, altura_min, id_usuario)  
"""preferencias = {
    "carrera_de_preferencia": carrera_de_preferencia,
    "zona_de_interes": zona_de_interes,
    "estilo_musical_de_preferencia": estilo_musical_de_preferencia,
    "hobbie_de_interes": hobbie_de_interes,
    "altura_minima": altura_minima,
    "altura_maxima": altura_maxima,
    "edad_minima": edad_minima,
    "edad_maxima": edad_maxima
}
"""
#match = obtener_match(df,id_usuario,candidatos, preferencias)
    
    
    
    
    
    
    
    
    
    
    
    
    
    