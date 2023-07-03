#**************************************************************************
# * Name: Lorenzo Anagnost                                          CSC 157
# * Date: 7/2/2023                                                  LAB 4   
# *************************************************************************
# * Problem Statement and Specifications: 
# *         Complete the methods in this file
# * 
# * Input:  N/A
# *
# * Output: Sentence with the number of vowels in it, and a rectangle
# *         made of an ASCII characters.
# *
# *************************************************************************

# ****** COMPLETE THE FOLLOWING METHODS BELOW ******

# @param input a string   
# Precondition: input must be a non-empty string 
# Postcondition: display the input string, the number of characters in the input string, 
# as well as the counts for all vowel types in the input string. 
def display_vowel_info(input):
    A=0
    E=0
    I=0
    O=0
    U=0
    newInput = input.upper()
    for letter in newInput:
        if letter == "A":
            A+=1
        elif letter == "E":
            E+=1
        elif letter == "I":
            I+=1
        elif letter == "O":
            O+=1
        elif letter == "U":
            U+=1
    print(f"The sentence \"{input}\" has {len(input)} characters, and there are")
    print(f"{A} a's\n{E} e's\n{I} i's\n{O} o's\n{U} u's")

# @params base the base length of the rectangle as a positive integer
#         height the height of the rectangle as a positive integer
#         character the character used to print the rectangle  
# Precondition: base and height must be positive integers, character must be a valid
#               keyboard character
# Postcondition: prints the rectangle with dimensions base x height using the
#                specified character
def print_rectangle(base, height, character):
    for h in range(height):
        for b in range(base):
            print(character, end="")
        print()
    
# @params theList a list of numerical values
# @return the number of negative numbers in the list           
# Precondition: theList is non-empty 
# Postcondition: returns number of negatives
def num_negatives(theList):
    counter=0
    for n in theList:
        if n < 0:
            counter = counter + 1
    return(counter)
    
# @params theList a list of numerical values
# @return a list containing only the negative numbers in the list           
# Precondition: theList is non-empty 
# Postcondition: returns a list of all negative numbers in the list
def negatives(theList):
    res = []
    for n in theList:
        if n < 0:
            res.append(n)
    return res
