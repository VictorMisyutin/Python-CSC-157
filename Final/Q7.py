import random
n1 = random.randint(100,999)
n2 = random.randint(100,999)
answer = n1+n2
response = int(input(f"Add these two numbers:\n  {n1}\n+ {n2}\n"))
if response == answer:
    print("congratulations you got it right!")
else:
    print(f"Sorry that was incorrect, the correct answer was {answer}")