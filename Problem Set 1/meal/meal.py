def main():
  myInput = str(input("What time is it? "))
  decTime = convert(myInput)
  response = calculateResponse(decTime)
  if response:
    print(response)
  
def convert(time):
  parts = time.split(":")
  h = int(parts[0])
  m = int(parts[1])
  return h+float(m/60)
  
def calculateResponse(decTime):
  if 18 <= decTime <= 19:
    return "dinner time"
  if 12 <= decTime <= 13:
    return "lunch time"
  if 7 <= decTime <= 8:
    return "breakfast time"
  
main()