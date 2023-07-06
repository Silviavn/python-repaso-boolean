import time
# Ejercicio. Hacer un programa que parta contando regresivamante desde 10 y que al llegar a cero diga "Boooom"
# Tip: esperar un segundo entre cada iteración utilizando time.sleep(1)

# 10
# 9
# 8
# ...
# Booom
num = 10
while num >= 0:
  print(num)
  num = num - 1
  time.sleep(1)

print("Booom")
print(num)