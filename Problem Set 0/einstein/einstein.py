def main():
  print("E:", calculateEnergy(int(input("m: "))))

def calculateEnergy(myInt):
  return myInt * 300000000 ** 2

main()