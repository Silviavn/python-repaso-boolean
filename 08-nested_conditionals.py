# Una evaluación condicional puede estar dentro de otra. Por ejemplo:
name = input("Hola, cuál es tu nombre? ")
age = int(input("Dime tu edad: "))

print(f"Hola {name}!")

if(age >= 18):
    drink = input("¿Quieres cerveza o vino?")
    if(drink) == "cerveza":
        print("Toma: ")  
        print("Aquí tienes tu Cerveza")
    else:
        print("Acá está tu vino")
else:
    juice = input("¿Quieres jugo de frutilla o naranja?")
    if(juice == "frutilla" or juice == "frutillas"):
        print("Acá está tu jugo de fresas")
    else:
        print("Toma tu jugo de naranjas")