def main():
  myInput = str(input("What is the Answer to the Great Question of Life, and Everything? "))
  print(answerQuestion(myInput))
  
def answerQuestion(question):
  answer = ["42", "forty-two", "forty two"]
  if question.lower() in answer:
    return "Yes"
  else:
    return "No"

main()