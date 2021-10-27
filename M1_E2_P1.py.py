""""**********************************
Autor       : Bristela Muñoz Burgos
Carrera     : Ingeniería en Informática
Ramo        : Programación Básica
Modulo      : M1-E2
Ejercicio 1 :
   Crear un programa que dibuje una matriz, según las siguientes consideraciones:
    1. Solicitud de filas
    2. Solicitud de columnas
    3. Se logre dibujar filas indicadas
    4. Se logre dibujar columnas solicitadas.
    Por ejemplo para una matriz de 4 x 4, el ejercicio debe retornar lo siguiente"""
""""**********************************
"""

# Con ciclos anidados porque en uno tenemos que manejar columnas y en otro filas

# Primero creamos una matriz (columnas en filas)
columnas = input("indique columnas")
columnas =int(columnas)
filas = input("indique filas")
filas =int(filas)
j=0
i=0
#luego crearemos un bucle para las filas y columnas ingresadas
#print("+----",end="") <= para lograr que impresion se repita hacia al lado, es decir (,end="")
#print("+")<= significa que salto para imprimir "|" , es decir print("|    ",end=""), también hacia el lado
#con esto ya logro que la serie se repita para conformar la estructura ordenada (matriz)
#ahora solo nos falta cerrar para completar la matriz, lo que logramos con un "for"
#para cerrar la estructura (ultima columna en "+----")=>print("+----",end="")

for i in range(filas):
    for j in range(columnas):
        print("+----",end="")
    print("+")
    for j in range(columnas):
        print("|    ",end="")
    print("|")
for j in range(columnas):
    print("+----",end="")
print("+")









