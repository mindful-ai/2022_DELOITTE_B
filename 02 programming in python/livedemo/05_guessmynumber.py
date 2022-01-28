# Design a Guess my Number game


# Banner
# Computer -> I have a number, can you guess? (45)
# Your guess > 40
# In correct. Guess Higher
# Your guess > 50
# In correct. Guess lower
# Your guess > 45
# Congratulations!
# ---------------------------------
# Result: Excellent (3) Good (7) Need Improvement(>7) Max trials (10)
# Question? What is the range? (1 - 100)

import random

# Print the banner
print("-"*50)
print("\t\tGUESS MY NUMBER")
print("-"*50)
print("The computer will pick a number between 1 and 100")
print("You are supposed to guess that number")
print("-"*50)
print("\n\nPicking a number....")

# Pick a random number between 1 and 100 -> rnum
rnum = random.randint(1, 100)

# Initialize trials
trials = 0

# Gaming loop (max trials == 10)
while trials <= 10:

    # Prompt the user
    # Take the input from the user -> userin
    userin = int(input("Your guess > "))

    # compare userin and rnum
    if(userin == rnum):
        # if they are same, say congratulations and exit
        print("Congratulations!! You guessed it right")
        break
    else:
        # if they are not same, give a message to the user, increment the trials
        if(userin > rnum):
            print("Incorrect. Guess something lower")
        elif(userin < rnum):
            print("Incorrect. Guess something higher")

        trials += 1

# Results
print("-"*50)

if(trials <= 3):
    print("Excellent Playing!!")
elif(3 < trials <= 7):
    print("Good")
else:
    print("Better luck next time!")

if(input("Do you want to display trials (y/n) ? ").lower() == 'y'): 
    print("Trials taken : ", trials)
        
print('THANK YOU!')