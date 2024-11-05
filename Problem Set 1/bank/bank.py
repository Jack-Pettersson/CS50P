def main():
  myInput = str(input("Greeting: "))
  print(calculateResponse(myInput))
  
def calculateResponse(greeting):
  firstWord = greeting.split(" ")[0].lower()
  firstWord = ''.join(e for e in firstWord if e.isalnum())

  if firstWord == "hello":
    return "$0"
  elif firstWord[0] == "h":
    return "$20"
  else:
    return "$100"
  
main()