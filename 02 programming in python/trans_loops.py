Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # --------- Loops
>>> 
>>> print('5 ', ' X ', ' 1 ', ' = ', '5')
5   X   1   =  5
>>> 
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> for i in range(1, 11):
	print('5 ', ' X ', ' 1 ', ' = ', '5')

	
5   X   1   =  5
5   X   1   =  5
5   X   1   =  5
5   X   1   =  5
5   X   1   =  5
5   X   1   =  5
5   X   1   =  5
5   X   1   =  5
5   X   1   =  5
5   X   1   =  5
>>> for i in range(1, 11):
	print('5 ', ' X ', i , ' = ', 5*i)

	
5   X  1  =  5
5   X  2  =  10
5   X  3  =  15
5   X  4  =  20
5   X  5  =  25
5   X  6  =  30
5   X  7  =  35
5   X  8  =  40
5   X  9  =  45
5   X  10  =  50
>>> 
>>> for c in "python":
	print(c)

	
p
y
t
h
o
n
>>> for item in ["red", "green", "blue"]:
	print(item.upper(), end=' ')

	
RED GREEN BLUE 
>>> 
>>> for i in range(1, 11):
	if (i % 5 == 0):
		break
	print('5 ', ' X ', i , ' = ', 5*i)

	
5   X  1  =  5
5   X  2  =  10
5   X  3  =  15
5   X  4  =  20
>>> for i in range(1, 11):
	if (i % 3 == 0):
		continue
	print('5 ', ' X ', i , ' = ', 5*i)

	
5   X  1  =  5
5   X  2  =  10
5   X  4  =  20
5   X  5  =  25
5   X  7  =  35
5   X  8  =  40
5   X  10  =  50
>>> 
>>> 
>>> i = 1
>>> while i <= 10:
	print('5 ', ' X ', i , ' = ', 5*i)
	i = i + 1

	
5   X  1  =  5
5   X  2  =  10
5   X  3  =  15
5   X  4  =  20
5   X  5  =  25
5   X  6  =  30
5   X  7  =  35
5   X  8  =  40
5   X  9  =  45
5   X  10  =  50
>>> 
