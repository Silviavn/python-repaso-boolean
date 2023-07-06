# Una de las características más poderosas de los lenguajes de programación como Python, es su habilidad para manipular variables. Una variables es simplemente un nombre que referencia o apunta a un valor. Como su nombre lo indica, el valor de la variable puede ir cambiando.

# Las variables permiten mantener valores en la memoria del computador
name = "Estudiando Python"

name = name + "!"

# Reasignación de variable. Ahora la variable apunta a un valor completamente diferente
name = "Hola Mundo"

print(name)

# Los nombres de las variables pueden contener letras, números, pero no pueden partir con números. Las mayúsculas y minúsculas son importantes, por lo que NAME, name y Name, son tres variables diferentes.

NAME = "SoyMás"
name = "Python"
Name = "Code"

print("Hola", NAME,name,Name)

people = 4
tables = 5
# Print puede recibir varias variables, cada una separada por ","
print(people,tables)
# También puede recibir expresiones utilizando variables
print(people*tables)

# Las variables no pueden coincidir con alguna palabra reservada del mismo lenguaje.
# Por ejemplo, sería una mala idea llamar a una variable "print"
# https://flexiple.com/python/python-reserved-words/
