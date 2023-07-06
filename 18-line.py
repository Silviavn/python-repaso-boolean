for row in range(10): 
  line = ""
  for col in range(10):
    if(row == 0 or row == 9):
      line += "*"
    elif(col == 0 or col == 9):
      line += "*"
    else:
      line += " "
  print(line)