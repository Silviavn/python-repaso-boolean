# Python nos da metodos para operar sobre las listas.Por ejemplo podriamos agregar  un nuevo elemento al final de la lista con el metodo append()

letters = ['a','b','c']
letters.append('x')

print(letters)

#Tambien podemos agregar los elementos de una lista a otra utilizando el metodo extend()

more_letters = ['m','n','o','p',]
letters.extend(more_letters)

print(letters)

#el metodo sort () ordena los elementos de forma ascendente

other_letters = ['d','a','e','g','b']
other_letters.sort()
print(other_letters)