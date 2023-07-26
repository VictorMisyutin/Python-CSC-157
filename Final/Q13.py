userIn = input("Please enter a date in this form: (month, in numeric form)/(day)/(a two-digit year):\n")
try: 
    temp = userIn.split("/")
    month = int(temp[0])
    day = int(temp[1])
    year = int(temp[2])
    if (month > 0 and month < 13) and (day > 0 and day < 32) and (year >= 0 and year < 100):
        if (month*day == year):
            print("The date is magic!")
        else:
            print("The date is not magic.")
    else:
        print("You did not enter a valid date.")
except:
    print("You did not enter a valid date.")
