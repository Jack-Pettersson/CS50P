def main():
  myInput = str(input("Expression: "))
  print(calculate(myInput))
  
def calculate(expression):
  parts = expression.split(" ")
  x = int(parts[0])
  y = str(parts[1])
  z = int(parts[2])
  
  if y == "+":
    return round(float(x+z), 1)
  elif y == "-":
    return round(float(x-z), 1)
  elif y == "*":
    return round(float(x*z), 1)
  elif y == "/":
    return round(float(x/z), 1)
  
main()