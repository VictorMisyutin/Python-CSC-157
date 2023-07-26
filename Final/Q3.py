def sentenceConverter(sentence):
   newString = ""
   prev = 0
   for i in range(0,len(sentence)):
       if(sentence[i] == sentence[i].upper()):
           newString += sentence[prev:i] + " "
           prev = i
   newString += sentence[prev:len(sentence)]       
   return (newString[1] + newString[2:len(newString)].lower())


def main():
    new = sentenceConverter("StopAndSmellTheRoses")
    print(new)

if __name__ == "__main__":
    main()