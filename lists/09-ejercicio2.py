#Calcular el promedio /

notas = [2.0, 5.5, 7.9, 4.0, 4.4] 
nota = 0
cantidad_notas = 5

for promedio in notas:
 nota += notas / cantidad_notas
print (nota) 

print("el promedio de los numeros es:")


notas = [2.0, 5.5, 7.9, 4.0, 4.4]
suma_notas = 0
cantidad_notas = len(notas)

for nota in notas:
    suma_notas += nota

promedio = suma_notas / cantidad_notas
print("El promedio de los números es:", promedio)