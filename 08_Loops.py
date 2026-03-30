#Loops
a = int(input("Enter the value of a \n"))
b = 1
while b<11:
    print(a,"*",b,"=",a*b)
    b += 1

for i in range(1,6):
    print(i)
for i in["Ali","Ahmed"]:
    print(i)

#Guessing Game
import random
jackpot = random.randint(1,100)
guess = int(input("Enter the number"))
count = 1
while guess != jackpot:
    if guess < jackpot:
        print("Guess Higher")
    else:
        print("Guess Lower")
    guess = int(input("Try Again"))
    count += 1
print("Correct guess")
print("You took",count,"attempts to guess the number correctly")

for i in range(1,6):
  for j in range(0,i):
    print("*",end=" ")
  print("")