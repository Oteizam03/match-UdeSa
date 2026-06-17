def grafico_match(matches):
    
    '''
    Esta funcion tiene el objetivo de tomar los datos del calculo de match, donde\
    se obtienen los usuarios con los que se matchea y el porcentaje de match con cada\
    uno. De esta manera, se ordenan de mayor a menor los porcentajes de cada usuario \
    y se construye un grafico de barras horizontales (a partir de la libreria matplotlib)\
    siendo el primer usuario el de mayor coincidencia. Por otro lado con los datos \
    obtenidos del calculo de match se crea un mensaje donde se indican los usuarios y el resto de los datos. 
    
    Parametros:
    matches: src, lista.
    Va a recibir una lista de datos de los usuarios donde se toman los legajos y porcentajes
    
    Return:
    mensaje: src.
    Va a establecer secciones de cada usuario con los datos de cada uno. 
    Ademas se muestra el grafico al finalizar la funcion gracias al metodo .show()

    '''
    import matplotlib.pyplot as plt
    print(matches[0])
    cantidad_por_porcentaje = {}

    for m in matches:
        porcentaje = m["puntaje"]
    
        if porcentaje in cantidad_por_porcentaje:
            cantidad_por_porcentaje[porcentaje] += 1
        else:
            cantidad_por_porcentaje[porcentaje] = 1
    
    porcentajes_ordenados = sorted(
    cantidad_por_porcentaje.keys(),
    reverse=True)
    
    porcentajes = porcentajes_ordenados
    cantidades = []

    for porcentaje in porcentajes_ordenados:
        cantidades.append(cantidad_por_porcentaje[porcentaje])
    
    plt.figure()
    plt.barh(porcentajes, cantidades, color = "pink")
    plt.title("Grafico de matches")
    plt.xlabel("Cantidad de usuarios")
    plt.ylabel("Porcentaje match")
    plt.gca().invert_yaxis() # IA me ayudo a hacer que el primer match sea el de mayor coincidencia
    plt.show()
    
    
    matches_ordenados = sorted(
    matches,
    key=lambda x: x["puntaje"],
    reverse=True)
    mensaje = ""
    
    mensaje = "\n¡Hiciste match con estos usuarios!\n"
    mensaje += "==================================\n\n"

    for m in matches_ordenados:
        mensaje += (
            f"ID: {m['id']}\n"
            f"Nombre: {m['nombre']} {m['apellido']}\n"
            f"Porcentaje de match: {m['puntaje']}\n"
            f"Instagram: {m['instagram']}\n"
            f"Teléfono: {m['telefono']}\n"
            "----------------------------------\n"
            )

    return mensaje

