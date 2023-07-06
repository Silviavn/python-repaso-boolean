# Ejercicio. utilizando for y range, crear un algoritmo que imprima en la terminal las tablas de multiplicar desde el 1 al 12.

# La tabla del 1 es:
# 1 x 1 = 1
# 1 x 2 = 2
# .........

# La tabla del 2 es:
# 2 x 1 = 2
# 2 x 2 = 4
# .........

for table in range(1,13):
  print()
  print(f"La tabla del {table} es:")
  for step in range(1,13):
    print(f"{table} x {step} = {table*step}")