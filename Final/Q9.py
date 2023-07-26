file = open("number_list.txt","w")

for number in range(1,101):
    file.write(str(number)+"\n")

file.close()
