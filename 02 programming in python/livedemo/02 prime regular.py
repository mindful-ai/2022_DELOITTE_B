# project a:
# Write a program to determine if a number is prime or not

# input
n = int(input("Enter a number: "))

# process
prime = True
for i in range(2, (n//2 + 1)):
    if(n % i == 0):
        prime = False
        break

# output
if(prime == True):
    print("The number is prime")
else:
    print("The number is not prime")

    
