def main():
  print(convert(str(input())))

def convert(myString):
  myString = myString.replace(":)", "🙂")
  myString = myString.replace(":(", "🙁")
  return myString

main()