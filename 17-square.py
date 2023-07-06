# Tarea: Utilizando for e if dibujar un cuadrado en la terminal

for row in range(12):
  line = ""
  for col in range(12):
    if col == 0 or col == 11:
      line += "*"
    elif row == 0 or row == 11:
      line += "*"
    else:
      line += " "
  print(line)