fileName = input("Please enter the file name: ")
file = open(fileName, "r")
lineNum = 1
for line in file:
    print(f"{lineNum}:{line}",end="")
    lineNum += 1