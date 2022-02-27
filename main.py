import random
number = random.randint(1, 9)
chanceCount = 0
print("Number Guessing Game")
print("Guess a number (between 1 and 9)")
while (chanceCount < 5):
    enteredNo = int(input("Enter your number:- "))
    if (enteredNo > number):
        print("Your guess is too large: Guess a number less than " , enteredNo)
    elif (enteredNo == number):
        print("Congratulation YOU WON !!!!!!")
      
    else :
        print("Your number guess is too low : Guess a number greater than", enteredNo)
    chanceCount = chanceCount + 1
if not chanceCount < 5:
    print("You Lose! The the number is ", number)
