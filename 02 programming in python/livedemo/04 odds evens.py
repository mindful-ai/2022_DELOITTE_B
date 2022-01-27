# Get some numbers from the user
# separate the odd number and even numbers

# Input:
# > 1 2 3 4 5 6 7
# Output:
# Evens: 2 4 6
# Odds: 1 3 5 7

# input

uin = input("Enter your numbers: ")

# process

evens = []
odds = []
numbers = uin.split()
for n in numbers:
    temp = int(n)
    if(temp % 2 == 0):
        evens.append(n)
    else:
        odds.append(n)

# output

print("-"*30)
print("EVENS : ", ' '.join(evens))
print("ODDS  : ", ' '.join(odds))
