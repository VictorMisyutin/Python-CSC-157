#**************************************************************************
# * Name: Victor Misyutin                                           CSC 157
# * Date: 7/4/2023                                                  LAB 5   
# *************************************************************************
# * Problem Statement and Specifications:  
# * 
# * 
# * Input: a sentence
# *
# *
# * Output: the same sentence but shortened
# *
# *
# *************************************************************************

sentence = input("Type the message to be shortened")

vowels = ["A", "E", "I", "O", "U"]

#algorithm 1
print("Algorithm 1")
vowelCount = 0
repeatCount = 0
length = len(sentence)
for i in range(length):
    letter = sentence[i]
    if letter == "A" or letter == "a" or letter == "E"or letter == "e" or letter == "I" or letter == "i" or letter == "O" or letter == "o" or letter == "U" or letter == "u":
        if letter[i] == letter[i-1]:
            repeatCount = repeatCount +1
            sentence = sentence[0:i-1] + sentence[+1:len(sentence)] 
            i = i-1       
        if i == 1 or [i-1] == " ":
            sentence = sentence[0:i-1] + sentence[+1:len(sentence)]        
            vowelCount = vowelCount + 1
            i = i-1

print(f"Vowels Removed {vowelCount}")
print(f"Repeats Removed {repeatCount}")
print(f"Algorithm 1 message: {sentence}")
print(f"Algorithm 1 characters saved: {vowelCount+repeatCount}")

#algorithm 2
print("Algorithm 2")
