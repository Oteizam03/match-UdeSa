url = r"datos/dataframe.xlsx" 

from src.mostrar_menu import mostrar_menu
from src.bienvenida import mostrar_bienvenida
from src.filtrado import filtrar_usuarios
from src.calculo_match import obtener_match
from src.Graficos import grafico_match
from src.pedir_preferencias import pedir_preferencias
from src.validar_usuario import validar_usuario
from src.cargar_datos import cargar_datos
from src.Graficos import grafico_zonas

df = cargar_datos(url)
mostrar_bienvenida()
opcion = ""
while True: 
    if opcion == "3":
        print("\nListo, nos vemos! Suerte en el amor.")
        break 
    opcion = mostrar_menu()
    
    if opcion == "2": 
        while True: 
            try:
              id_usuario = input("\nIngrese el numero de id/legajo, son 5 numeros: ").strip()
              validar_usuario(df, id_usuario) 
              
              fila = df[df["id"] == (id_usuario)] 
              nombre = fila["nombre"].values[0]
              apellido = fila["apellido"].values[0]
              print("\nBienvenido", nombre, apellido, "esperemos que encuentres el amor y seas feliz") 
              
              edad_minima, edad_maxima, altura_minima, altura_maxima, hobbie_de_interes, estilo_musical_de_preferencia, zona_de_interes, carrera_de_preferencia = pedir_preferencias(df)   
                
            except ValueError as e:
                print(e) 
                print("\nPor favor vuelva a ingresar los datos otra vez")
            
            else:
                print("\nLos datos fueron cargados correctamente") 
                break
        #con esto consigo los parametros para correr la funcion
        fila = df[df["id"] == id_usuario].iloc[0]
        genero = fila["sexo"]
        sexualidad = fila["sexualidad"]
        
        preferencias = {
            "carrera_de_preferencia": carrera_de_preferencia,
            "zona_de_interes": zona_de_interes,
            "estilo_musical_de_preferencia": estilo_musical_de_preferencia,
            "hobbie_de_interes": hobbie_de_interes,
            "altura_minima": altura_minima,
            "altura_maxima": altura_maxima,
            "edad_minima": edad_minima,
            "edad_maxima": edad_maxima
            }
        
        candidatos = filtrar_usuarios(df, genero, sexualidad, edad_minima, edad_maxima, altura_minima, altura_maxima, id_usuario)
        
        try: 
            matches = obtener_match(df,id_usuario,candidatos, preferencias)
            if len(matches) == 0:
                print("La lista no puede estar vacía")
            mensaje = grafico_match(matches)
            grafico_zonas(matches)
            print(mensaje)
        except ValueError as e:
            print("Error:", e)
        #break      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        #continuar= input("Te gustaria continuar o deseas terminar? ")
        while True:
            continuar= input("\nTe gustaria continuar o deseas terminar? ")
            if continuar.strip().lower() == "continuar":
                break
            elif continuar.strip().lower() == "terminar": 
                opcion = "3"
                break
            else:
                print("\nERROR, respuesta incorrecta. No era una opcion")
                
                
            
            
      
            
    elif opcion == "1": 
        mostrar_bienvenida()
    
    elif opcion == "3":
        print("\nListo, nos vemos! Suerte en el amor 💘")
        break 
    else: 
        print("\nERROR, opcion invalida. Ingrese 1, 2 0 3")  
        