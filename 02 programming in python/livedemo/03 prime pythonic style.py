# project a:
# Write a program to determine if a number is prime or not

# input
n = int(input("Enter a number: "))

# Process/OUtput

for i in range(2, (n//2 + 1)):
    if(n % i == 0):
        print("The number is not prime")
        break
else:
    print("The number is prime")
