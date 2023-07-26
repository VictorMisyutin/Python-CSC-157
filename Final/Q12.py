file = open("textFile.txt", "r")
dict = {}
tempList = []
for line in file:
    list = line.split()
    for word in list:
        word = word.lower()
        if word in dict:
            dict[word] +=1
        else:
            dict[word] = 1

for key in dict:
    print(f"\"{key}\" appears {dict[key]} times.")
