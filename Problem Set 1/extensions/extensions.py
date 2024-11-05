def main():
  myInput = str(input("File name: "))
  print(returnMediaType(myInput))
  
def returnMediaType(fileName):
  allowedExtensions = ["gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"]
  fileTypeDict = {
    "gif":"image/gif",
    "jpg":"image/jpeg",
    "jpeg":"image/jpeg",
    "png":"image/png",
    "pdf":"application/pdf",
    "txt":"text/plain",
    "zip":"application/zip"
  }
  extension = fileName.split(".", -1)[-1].lower()

  if extension in allowedExtensions:
    return fileTypeDict[extension]
  else:
    return "application/octet-stream"
  
main()