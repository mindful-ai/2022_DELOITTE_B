# A calculator program

'''
CALCULATOR

----------------------------

A = 34
B = 76

Options:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide

Your option : 1

----------------------------

RESULT: 110
'''

print("CALCULATOR")
print("-"*30)

# input
a = int(input("A = "))
b = int(input("B = "))

print("Options")
print("\t1. Add")
print("\t2. Subtract")
print("\t3. Multiply")
print("\t4. Divide")

option = input("Your option: ")

# process

if(option.isdigit() and 1 <= int(option) <= 4):
    if(option == '1'):
        result = a + b
    elif(option == '2'):
        result = a - b
    elif(option == '3'):
        result = a * b
    else:
        result = a / b
else:
    print("Invalid option!")

# output

print("-"*30)
print("RESULT : ", result)
