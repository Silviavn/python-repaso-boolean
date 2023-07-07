#Los slices osn como rebanadas de una lista o segmentos y se utilizan con el simpolo :
letters = ['a','b','c','d','e','f','g']

print(letters[1:3]) #como resultado b y c

#Parte de en el primero y termina en el indice previo al ultimo, en este caso seleccionara desde el indice uno al dos

print(letters[:4]) #como resultado nos da 

print(letters[3:]) #como resultado nos da 

#con los slices tambien podriamos modificar varios valores

letters[1:3] = ['x', 'y']
print(letters)
 #como resultado nos da 



