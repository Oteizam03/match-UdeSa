import matplotlib.pyplot as plt

#from src.calculo_match import calculo_match # ESTO VA en el main
## matches = calculo_match()
#mensaje = grafico_de_matches(matches)
#print(mensaje)## ESTO VA EN EL MAIN

def grafico_match(matches):
    
    '''
    Esta funcion tiene el objetivo de tomar los datos del calculo de match, donde\
    se obtienen los usuarios con los que se matchea y el porcentaje de match con cada\
    uno. De esta manera, se obtiene un grafico en orden donde se puede ver primero \
    el usuario que mas coincidencia tiene en relacion a las preferencias del usuario.

    '''
    
    matches_ordenados = sorted(  # IA me ayudo a hacer que el primer match sea el de mayor coincidencia
    matches,
    key=lambda x: x[1],
    reverse=True)
    
    
    ids = [m["id"] for m in matches_ordenados]
    porcentajes = [m["porcentaje"] for m in matches_ordenados]

    plt.figure()
    plt.barh(porcentajes, ids, color = "pink")
    plt.title("Grafico de matches")
    plt.xlabel("Usuarios")
    plt.ylabel("Porcentaje match")
    plt.gca().invert_yaxis() # IA me ayudo a hacer que el primer match sea el de mayor coincidencia
    plt.show()
    
    mensaje = ""
    
    mensaje = "\n¡Hiciste match con estos usuarios!\n"
    mensaje += "==================================\n\n"

    for m in matches_ordenados:
        mensaje += (
            f"ID: {m['id']}\n"
            f"Nombre: {m['nombre']} {m['apellido']}\n"
            f"Porcentaje de match: {m['porcentaje']}%\n"
            f"Instagram: {m['instagram']}\n"
            f"Teléfono: {m['telefono']}\n"
            "----------------------------------\n"
            )

    return mensaje

