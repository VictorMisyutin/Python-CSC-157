#**************************************************************************
# * Name: Victor Misyutin                                           CSC 157
# * Date: 18-6-2023                                                 LAB 3  
# *************************************************************************
# * Problem Statement and Specifications: Ask user for their name and then
# *     ask them to guesse 3 different numbers. If they guess all 3 numbers 
# *     with the correct criteria then they win, else end the code. 
# * Input:  
# *     Users name, Phase 1 number, Phase 2 number, and Phase 3 number
# *
# * Output: 
# *     Their name with "are you ready to crack the code?".
# *     "Correct" if they guess that phases number correctly or 
# *     "Sorry, that was incorrect Better luck next time!" if they do not.
# *     Print "You have cracked the code!" if they guess all numbers correctly.
# *************************************************************************

print("Welcome. What is your name?")
name = input()
print(f"Hello {name}. Are you ready to crack the code?")
answer = input()
answer = answer.upper()
if answer == "YES":
    print("\nPHASE 1\nEnter a number:")
    response = input()
    if response == "3":
        print("Correct")
        print("\nPHASE 2\nEnter a number:")
        response = int(input())
        if response == 1 or (response >=33 and response <= 100):
            print("Correct!")
            print("\nPHASE 3\nEnter a number:")
            response = int(input())
            if (response > 0 or (response%3==0 or response%7==0)):
                print("Correct!")
                print("You have cracked the code!")
            else:
                print("Sorry, that was incorrect!\nBetter luck next time!")
        else:
            print("Sorry, that was incorrect!\nBetter luck next time!")
    else:
        print("Sorry, that was incorrect!\nBetter luck next time!")