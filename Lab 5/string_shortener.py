#**************************************************************************
# * Name: Victor Misyutin                                           CSC 157
# * Date: 7/4/2023                                                  LAB 5   
# *************************************************************************
# * Problem Statement and Specifications:  Given a sentence that is inputed
# *     by the user, use two different algorithms to shorten that sentence.
# * 
# * Input: a sentence
# *
# *
# * Output: the same sentence but shortened
# *
# *
# *************************************************************************

sentence = input("Type the message to be shortened\n")
sentence1 = sentence
sentence2 = sentence
#algorithm 1
print("\nAlgorithm 1")
vowelCount = 0
repeatCount = 0
length = len(sentence1)
count = 0
i = 1
while i < length and count < 1000:
    count = count+1
    letter = sentence1[i]
    if letter == "A" or letter == "a" or letter == "E"or letter == "e" or letter == "I" or letter == "i" or letter == "O" or letter == "o" or letter == "U" or letter == "u":
        if(sentence1[i-1] != " "):
            vowelCount = vowelCount+1
            sentence1 = sentence1[0:i] + sentence1[i+1:len(sentence1)]
            i = i-1
    elif letter == sentence1[i-1]:
        repeatCount = repeatCount +1
        sentence1 = sentence1[0:i] + sentence1[i+1:len(sentence1)]
        length = len(sentence1)
        i = i-1
    i = i+1
    length = len(sentence1)

    

print(f"Vowels Removed {vowelCount}")
print(f"Repeats Removed {repeatCount}")
print(f"Algorithm 1 message: {sentence1}")
print(f"Algorithm 1 characters saved: {vowelCount+repeatCount}")

#algorithm 2
print("\nAlgorithm 2")
sentence3 = sentence2.replace(" ", "")
sentence3 = sentence3.lower()
res = {}
str = ""
for j in sentence3:
    if j in res:
        res[j] += 1
    else:
        res[j] = 1

count = 0 
for key in res:
    count += 1
print(f"Unique characters found: {count}")

print("Algorithm 2 message: ", end="")
for key in res:
    print(res[key], end="")
    print(key, end="")
print()
print(f"Algorithm 2 character saved = {len(sentence2) - count - len(res.values())}" )