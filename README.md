# Match Udesa

Integrantes: Milagros Oteiza, Uma Poggi, Sol Collins, Justo Barbosa, Victoria Azpeitia.



1. Objetivo:

El objetivo de este programa es que los alumnos de la Universidad de San Andres sean capaces de encontrar una pareja dentro de la facultad. La idea es tomar un usuario que ingresa su legajo y las preferencias que tienen en su pareja; con los datos almacenados en un dataset se encontrarán las coincidencias entre los datos de los alumnos y las preferencias. Finalmente se devuelve aquellos alumnos con los que se coincide (se hizo match) y un grafico que muestre los porcentajes de coincidencias. 

El programa se compone de 7 archivos con diferentes funciones, con la idea de que se integren en el main y puedan llevar a cabo el programa.

Si bien todos participamos en el diseño del trabajo, para facilitar decidimos dividir tareas.

El main y la validación del usuario fue elaborado por Sol.

El pedido y la validación de preferencias fue elaborado por Milagros.

La carga de datos y el filtrado fue elaborado por Justo.

El calculo de match fue elaborado por Uma.

El grafico y readme fue elaborado por Victoria.



2\. Descripción de la fuente de datos:

La fuente de datos es un DataFrame de 1500 registros que simula una API institucional con los legajos y diferentes datos personales de los alumnos de la universidad. Este incluye: Legajo, género, nombre, apellido, edad, zona en la que reside, hobbies, gusto de estilo musical, sexualidad, el teléfono y el Instagram.



3\. Instrucciones de ejecución:

Al iniciar el programa se preguntará el número de legajo y las preferencias del usuario en relación con su futura pareja. Luego se llevarán a cabo las funciones correspondientes de validación, carga y filtrado de datos para poder realizar el cálculo del match (porcentaje de coincidencia con los diferentes usuarios) y la ejecución de un gráfico que represente los niveles de match.



4\. Librerías utilizadas:

Pandas para el desgolzado del DataFrame y Matpolotlib.pyplot para el gráfico. 



5\. Estructura del repositorio:

Se compone de 3 carpetas, un readme y un main. Las carpetas son de datos (incluye el DataFrame), el diseño (diagramas y documentación) y el src (incluye los archivos de código).



6\. Funciones principales:

...



7\. Resultados, salidas, métricas, gráficos o funcionalidades generadas:

Los resultados finales del programa van a ser un mensaje con los datos de los usuarios de coincidencias (nombre, apellido, legajo, teléfono e Instagram) para que se contacte con sus matches si es que lo desea. Luego se muestra un gráfico donde se puede ver en orden de mayor a menor los niveles de porcentajes correspondientes a cada usuario. 

&#x20;

8\. Declaración de uso de IA:


...

