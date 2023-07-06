for row in range(1,15):
  # Al comienzo el row va a ser pequeño, partiendo de 1
  line = " " * row # Vamos aumentando la cantidad de " " por cada fila
  line += "* " * (15-row) # Vamos a ir disminuyendo los "* " por cada fila
  print(line) # Se imprime la linea que va cambiando la cantidad de espacios y asteriscos