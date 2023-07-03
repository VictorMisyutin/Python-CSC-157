#**************************************************************************
# * Name: Victor Misyutin                                           CSC 157
# * Date: 20-6-2023                                                 LAB 4   
# *************************************************************************
# * Problem Statement and Specifications: 
# *         Complete the methods in this file
# * 
# * Input:  N/A
# *
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
    a=0
    e=0
    i=0
    o=0
    u=0
    inputUpper = input.upper()
    for letter in inputUpper:
        match letter:
            case "A":
                a = a+1 
            case "E":
                e = e+1  
            case "I":
                i = i+1 
            case "O":
                o = o+1
            case "U":
                u = u+1 
    print(f"The sentence \"{input}\" has {len(input)} characters, and there are")
    print(f"{a} a's\n{e} e's\n{i} i's\n{o} o's\n{u} u's")

# @params base the base length of the rectangle as a positive integer
#         height the height of the rectangle as a positive integer
#         character the character used to print the rectangle  
# Precondition: base and height must be positive integers, character must be a valid
#               keyboard character
# Postcondition: prints the rectangle with dimensions base x height using the
#                specified character
def print_rectangle(base, height, character):
    for a in range(height):
        for b in range(base):
            print(character, end="")
        print()
    
# @params theList a list of numerical values
# @return the number of negative numbers in the list           
# Precondition: theList is non-empty 
# Postcondition: returns number of negatives
def num_negatives(theList):
    count=0
    for num in theList:
        if num < 0:
            count = count + 1
    return(count)
    
# @params theList a list of numerical values
# @return a list containing only the negative numbers in the list           
# Precondition: theList is non-empty 
# Postcondition: returns a list of all negative numbers in the list
def negatives(theList):
    newList = []
    for num in theList:
        if num < 0:
            newList.append(num)
    return newList
