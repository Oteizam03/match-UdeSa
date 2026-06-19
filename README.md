# Match Udesa

Integrantes: Milagros Oteiza, Uma Poggi, Sol Collins, Justo Barbosa, Victoria Azpeitia.

La informacion general del trabajo se encuentra tambien en el archivo "informacion del trabajo" dentro de la carpeta documentos.

1. Objetivo:

El objetivo de este programa es que los alumnos de la Universidad de San Andres sean capaces de encontrar una pareja dentro de la facultad. 
La idea es tomar un usuario que ingresa su legajo y las preferencias que tienen en su pareja; con los datos almacenados en un dataset se encontrarán las coincidencias entre los datos de los alumnos y las preferencias. 
Finalmente se devuelve aquellos alumnos con los que se coincide (se hizo match) y un grafico que muestre los porcentajes de coincidencias. 

El programa se compone de 9 archivos con diferentes funciones, con la idea de que se integren en el main y puedan llevar a cabo el programa.

Si bien todos participamos en el diseño del trabajo, para facilitar decidimos dividir tareas.

El DataFrame, la validación y pedido del usuario, y el pedido de preferencias fue elaborado por Milagros.

El main y la validación de preferencias fue elaborado por Sol.

las funciones de Milagros y Sol están conectadas para pedir y validar paso por paso. 

La carga de datos y el filtrado fue elaborado por Justo.

El obtener el match, el calculo de match y el menu fue elaborado por Uma.

Los gráficos, el mensaje de bienvenida y readme fue elaborado por Victoria.



2\. Descripción de la fuente de datos:

La fuente de datos es un DataFrame de 1500 registros que simula una API institucional con los legajos y diferentes datos personales de los alumnos de la universidad.
Este incluye: Legajo, género, nombre, apellido, edad, zona en la que reside, hobbies, gusto de estilo musical, sexualidad, el teléfono y el Instagram.
ACLARACION: se pueden usar DataFrames que tengan mas filas mientras se respeten las columnas. 
Ningún usuario real de UdeSA va a coincidir con los legajos del dataset dado que es un dataset de fantasia.


3\. Instrucciones de ejecución:


Al iniciar el programa se aparecerá una descripción del programa, es decir, su objetivo y qué datos se van a solicitar a continuación. Seguida de esta bienvenida aparece un menu en el que preguntamos si necesita de la explicación nuevamente, si quiere empezar el programa o si desea salir. En el caso que quiera ver de nuevo de que se trata va a seleccionar la opción 1 y va a aparecer el mensaje inicial. Luego si toca la opción 2 se inicia el programa que preguntará el número de legajo y las preferencias del usuario en relación con su futura pareja. Luego se llevarán a cabo las funciones correspondientes de validación, carga y filtrado de datos para poder realizar el cálculo del match (porcentaje de coincidencia con los diferentes usuarios) y la ejecución de un gráfico que represente los niveles de match. Terminado el proceso de búsqueda de match y muestra de mensaje se preguntara si desea terminar el programa o continuar. En el caso de querer terminarlo se muestra un mensaje de salida y se corta el programa y en caso de querer continuar va a mostrarse el menu inicial donde las opciones van a ser las mismas que antes (1 repetir objetivo e instrucciones, 2 iniciar el programa, 3 salir del programa). 

IMPORTANTE: para probar el programa fijarse que el numero de legajo este en el DataFrame (un ejemplo: 47672). Sino va a aparecer el error correspondiente a invalido. 


4\. Librerías utilizadas:

Pandas para el desgolzado del DataFrame y Matpolotlib.pyplot para el gráfico. 



5\. Estructura del repositorio:

Se compone de 3 carpetas, un readme y un main. Las carpetas son de "datos" (incluye el DataFrame), "documentos" en donde esta el diseño (diagramas y documentación) y el src (incluye los archivos de código).

Match_UdeSA/
│
├── main.py
├── requirements.txt
├── README.md
│
├── datos/
│   └── dataframe.xlsx
│
├── documentos/
│   ├── diagramas/
│   └── informacion_del_trabajo.md
│
└── src/
    ├── bienvenida.py
    ├── calculo_match.py
    ├── cargar_datos.py
    ├── filtrado.py
    ├── Graficos.py
    ├── mostrar_menu.py
    ├── pedir_preferencias.py
    ├── validar_preferencias.py
    └── validar_usuario.py

6\. Funciones principales:

cargar_datos: Carga un archivo .xlsx y lo retorna como un DataFrame de pandas

mostrar_bienvenida: Muestra el cartel de bienvenida y una explicacion corta del programa.

mostrar_menu: muestra el menú de opciones que tiene el usuario 

validar_usuario: valida que el legajo ingresado por el usuario sea correcto (que tenga 5 números y que exista dentro del DataFrame). Si no es valido levanta un ValueError. 

pedir_preferencias: Solicita y valida mediante las funciones de validar_preferencias las preferencias del usuario para buscar posibles matches.

validar_preferencias: son muchas funciones dentro de este archivo. Cada una valida el dato ingresado por el usuario (edad, altura, carrera, hobbit, etc.)

filtrar_usuarios: Filtra el DataFrame eliminando perfiles incompatibles con el usuario.

calculo_match: compara al candidato con las preferencias del usuario y calcula el porcentaje de compatibilidad. 

obtener_match: recorre los candidatos filtrados, calcula el porcentaje de compatibilidad y los agrupa en una lista. 

grafico_match: grafico de barras horizontales que muestra la cantidad de usuarios con los que tuviste cierto porcentaje de match. 

grafico_zonas: grafico de torta donde se puedan ver las zonas donde viven los usuarios con los que macheaste. 
    
...



7\. Resultados, salidas, métricas, gráficos o funcionalidades generadas:

Los resultados finales del programa van a ser un mensaje con los datos de los usuarios de coincidencias (nombre, apellido, legajo, teléfono e Instagram) para que se contacte con sus matches si es que lo desea. Luego se muestra un gráfico donde se puede ver los porcentajes de match y la cantidad de usuarios con lo que tuviste ese porcentaje, y un grafico de tortas que muestra las zona donde viven los usuarios con lo que tuviste match. 


8\. Declaración de uso de IA:

USO NUMERO 1: Uso de Milagros 

Explicacion del uso:
La IA se uso en primera instacia para armar un Dataframe con los datos que queriamos usar.
Lo moldeamos con nuestras preferencias y le pedimos al chat gpt que ponga datos aleatorios respetando nuestrar reglas.
Agregamos el prompt utilizado:
 "Generar un dataset en formato tabla (tipo pandas DataFrame o CSV) que represente usuarios de una aplicación tipo Tinder para estudiantes de UdeSa.
El dataset debe cumplir con las siguientes condiciones:

Columnas obligatorias:

legajo: identificador único de 5 dígitos (string)
nombre: nombre del estudiante
apellido: apellido del estudiante
edad: número entero entre 18 y 30
altura: número entero en cm (entre 100 y 230 aproximadamente)
genero: "M" o "F"
sexualidad: "heterosexual", "homosexual" o "bisexual"
carrera: debe ser una de las siguientes opciones (busca en la web todas las carreras de grado que tiene UDESA):
(abogacia, administracion de empresas, ciencia politica y gobierno, ciencias de la educacion, ciencias del comportamiento, comunicacion, contador publico, diseno, economia, economia empresarial, finanzas, humanidades, ingenieria en biotecnologia, ingenieria en inteligencia artificial, ingenieria en sustentabilidad, negocios digitales, profesorado en educacion primaria, relaciones internacionales)
hobbies: una de estas opciones:
(lectura, gaming, musica, arte, deporte)
estilo musical favorito: una de estas opciones:
(pop, reggaeton, rock, cumbia, clasica)
zona por la que vive: una de estas opciones:
(norte, centro, sur)

Reglas adicionales:

Debe haber variedad de géneros y sexualidades
Los legajos no deben repetirse
Los datos deben ser realistas (no todos iguales)
Debe haber al menos 1500 registros
Mezclar bien las combinaciones para que haya posibles matches

----------------------------------------------------------------
USO NUMERO 2: Uso de Uma Poggi Soqueff
explicacion de uso: No entendia porque el pregrama me tiraba un error en la funcion de calculo_match():
prompt : no estaria entendiendo el error que me tira en la linea del : if candidatos["carrera"] == preferencias["carrera_de_preferencia"]:
Chat me dijo que no podia comparar un dataframe con una lista, entonces me explico que si yo ponia el .lower() despues de: if candidatos["carrera"], osea en el programa queda if candidatos["carrera"].lower()== preferencias["carrera_de_preferencia"]:
si iba a poder ver comparar que la carrerara que haga el candidato esta dentro de mis preferencias.

----------------------------------------------------------------
USO NUMERO 3: Uso de Justo Barbosa Moreira
Explicacion de uso: Utilice claude para revisar la estructura de la función de filtrado y encarar las correcciones. Originalmente importabamos el dataframe a esa funcion, pero no era necesario ya que se hacia directamente en cargar_datos() de todos modos aproveche para que me marque posibles correciones en la estructura. Previo al prompt envie el documento del diseño para que sepa en que estaba trabajando
Prompt: yo me tengo que encargar de la parte de la funcion filtrado e hice esto:
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
el dataframe me parece que se puede borrar porque ya se abre directamente en el main #en ese momento del desarrollo del codigo abriamos desde el main, despues decidimos separarlo en otra funcion

----------------------------------------------------------------
USO NUMERO 4: Uso de Sol Collins

Explicación del uso: En el momento de validar los datos, si el usuario ingresaba una preferencia que tenia un error, ese error no aparecía hasta que el usuario no haya terminado de poner TODAS las preferencias. Lo que yo quería era que el error me aparezca justo despues de que el dato con el error haya sido ingresado. Estaba bloqueada y no se me ocurría como hacerlo, asi que le pedi ayuda a Claude. 

Prompt: Tengo este programa que le pide datos al usuario por consola. El problema es que cuando el usuario ingresa algo inválido, el error no aparece en el momento, sino recién después de que terminó de cargar TODOS los datos. Cómo puedo hacer para que la validación salte apenas se ingresa un dato incorrecto, en lugar de al final de todo? (Ademas del prompt, le subi todos los archivos de código del programa y el archivo de diseño)

----------------------------------------------------------------
USO NUMERO 5: Uso de Victoria Azpeitia
Explicación de uso: En IPC vimos gráficos entonces no hubo problemas en el armado del grafico pero era necesario arreglar detalles para que visualmente sea viable el gráfico. 

Prompt: Estamos haciendo un trabajo en grupo donde se busca un match dentro de nuestra facultad. Con esta base de datos, donde se encuentran los alumnos de la facultad, se analizan datos como el genero, altura, hobbies, sexualidad, etc y buscamos filtrar las preferencias para luego obtener un porcentaje de coincidencia. En mi caso tengo que hacer el mensaje final y un grafico de barras donde muestro la cantidad de usuarios que hay por cada porcentaje. Te mando como copile los datos pero necesito ayuda con cómo hacer para que se vea en orden de mayor a menor el porcentaje de match. 

Respuesta: 
- Para ordenar la lista de mayor a menor:
matches_ordenados = sorted(
    matches,
    key=lambda x: x[1],
    reverse=True
)

- Dentro del grafico:
plt.gca().invert_yaxis()  # mayor match arriba

----------------------------------------------------------------

uso en general cuando la consola nos tiraba un error para que nos ayude a comprender que significaba dicho error para luego poder pensar una solucion. 
el prompt consistia en mandarle una foto de la consola y una pregunta como: nos salto este error, me explicas en lenguaje basico que significa el error para que se me ocurra una solucion. 


