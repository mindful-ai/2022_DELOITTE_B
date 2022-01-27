Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # - ---------------- LISTS
>>> 
>>> L = ["red", "green", 1, -4.5, [1, 2, 3]]
>>> L
['red', 'green', 1, -4.5, [1, 2, 3]]
>>> type(L)
<class 'list'>
>>> 
>>> 
>>> # ------------------------------------------- Subscripting -> Access elements
>>> 
>>> L[0]
'red'
>>> L[1]
'green'
>>> L[-1]
[1, 2, 3]
>>> L[-1][2]
3
>>> L[-1][-1]
3
>>> L[1:3]
['green', 1]
>>> L[::2]
['red', 1, [1, 2, 3]]
>>> L[::-1]
[[1, 2, 3], -4.5, 1, 'green', 'red']
>>> 
>>> # ----------------------------------------- Mutability
>>> 
>>> L = ["red", "green", "blue"]
>>> L[1]
'green'
>>> L[1] = "yellow"
>>> L
['red', 'yellow', 'blue']
>>> 
>>> L[2]
'blue'
>>> L[2][1]
'l'
>>> L[2][1] = 'm'
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    L[2][1] = 'm'
TypeError: 'str' object does not support item assignment
>>> 
>>> # ---------------------------------- operators
>>> 
>>> [1,2,3] + [3, 4, 5]
[1, 2, 3, 3, 4, 5]
>>> 
>>> [1,2,3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> 
>>> len(L)
3
>>> "red" in L
True
>>> type(L) == list
True
>>> isinstance(L, list)
True
>>> 
>>> del L
SyntaxError: invalid syntax
>>> del L
>>> L
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    L
NameError: name 'L' is not defined
>>> 
>>> # ------------------------------- adding elements
>>> 
>>> L = ["red", "green", "blue"]
>>> L.append("yellow")
>>> L
['red', 'green', 'blue', 'yellow']
>>> L.append("orange")
>>> L
['red', 'green', 'blue', 'yellow', 'orange']
>>> 
>>> 
>>> L.insert(1, "golden")
>>> L
['red', 'golden', 'green', 'blue', 'yellow', 'orange']
>>> 
>>> L1 = ['black', 'white']
>>> L.extend(L1)
>>> L
['red', 'golden', 'green', 'blue', 'yellow', 'orange', 'black', 'white']
>>> 
>>> L = ["red", "green", "blue"]
>>> L[1]
'green'
>>> L[1] = L1
>>> L
['red', ['black', 'white'], 'blue']
>>> 
>>> L = ["red", "green", "blue"]
>>> L
['red', 'green', 'blue']
>>> L[1:2]
['green']
>>> L[1:2] = L1
>>> L
['red', 'black', 'white', 'blue']
>>> 
>>> # --------------------------------- removing elements
>>> 
>>> L
['red', 'black', 'white', 'blue']
>>> L.pop()
'blue'
>>> L
['red', 'black', 'white']
>>> L.pop(1)
'black'
>>> L
['red', 'white']
>>> 
>>> 'red' in L
True
>>> L.remove('red')
>>> L
['white']
>>> 
>>> 
>>> # --------------------------------------- re-arranging elements
>>> 
>>> L = ['red', 'black', 'white', 'blue']
>>> reversed(L)
<list_reverseiterator object at 0x0000018DCFDF4EB8>
>>> list(reversed(L))
['blue', 'white', 'black', 'red']
>>> L
['red', 'black', 'white', 'blue']
>>> L.reverse()
>>> L
['blue', 'white', 'black', 'red']
>>> 
>>> 
>>> sorted(L)
['black', 'blue', 'red', 'white']
>>> L
['blue', 'white', 'black', 'red']
>>> L.sort()
>>> L
['black', 'blue', 'red', 'white']
>>> L.sort(reverse=True)
>>> L
['white', 'red', 'blue', 'black']
>>> 
>>> 
>>> # ----------------------------------- search for elements
>>> 
>>> 'red' in L
True
>>> L.index('red')
1
>>> L.count('red')
1
>>> L.append('red')
>>> L.count('red')
2
>>> L
['white', 'red', 'blue', 'black', 'red']
>>> 
>>> # ---------------------------- iterating on the elements
>>> 
>>> L
['white', 'red', 'blue', 'black', 'red']
>>> for item in L:
	print(item)

	
white
red
blue
black
red
>>> for item in L:
	print(item, ' ----> ', len(item))

	
white  ---->  5
red  ---->  3
blue  ---->  4
black  ---->  5
red  ---->  3
>>> 
>>> # ---------------------------- in-built functions
>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(30, 40))
[30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
>>> list(range(1, 100, 5))
[1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96]
>>> list(range(10, 1, -1))
[10, 9, 8, 7, 6, 5, 4, 3, 2]
>>> 
>>> 
>>> L = [32, 45, 56, 78, 89]
>>> sum(L)
300
>>> 
>>> L = [True, True, False]
>>> any(L)
True
>>> range(10)
range(0, 10)
>>> L = list(range(10))
>>> L
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> any(L)
True
>>> all(L)
False
>>> all(L[1:])
True
>>> 
