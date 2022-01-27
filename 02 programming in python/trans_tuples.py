Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ["red", "green", "blue"]
>>> L[2] = "yellow"
>>> L
['red', 'green', 'yellow']
>>> type(L)
<class 'list'>
>>> 
>>> T = ("red", "green", "blue")
>>> type(T)
<class 'tuple'>
>>> T[2]
'blue'
>>> T[2] = "golden"
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    T[2] = "golden"
TypeError: 'tuple' object does not support item assignment
>>> # -------------------------- TUple are immutable in nature
>>> 
>>> T = ("red", "green", ["blak","white"], "yellow")
>>> T[2]
['blak', 'white']
>>> T[2].append("grey")
>>> T
('red', 'green', ['blak', 'white', 'grey'], 'yellow')
>>> 
>>> # Elements in the tuple need not be immutable
>>> 
>>> # ------------------- access elements using subscripts
>>> 
>>> # [start:end:interval]
>>> 
>>> # ------------------- adding, removing, re-arranging, replacing will not work
>>> 
>>> # ---------- re-arranging elements
>>> 
>>> T
('red', 'green', ['blak', 'white', 'grey'], 'yellow')
>>> sorted(T)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    sorted(T)
TypeError: '<' not supported between instances of 'list' and 'str'
>>> T = ("red", "green", "blue")
>>> sorted(T)
['blue', 'green', 'red']
>>> reversed(T)
<reversed object at 0x0000022E9AFD3EB8>
>>> tuple(reversed(T))
('blue', 'green', 'red')
>>> 
>>> # ------------- searching: in, index, count work well on tuples
>>> 
>>> 'red' in T
True
>>> T.count('red')
1
>>> T.index('red')
0
>>> # iteration with for loop works
>>> for item in T:
	print(T)

	
('red', 'green', 'blue')
('red', 'green', 'blue')
('red', 'green', 'blue')
>>> 
>>> # --------------- other functions: any(), all(), sum()
>>> T = (1, 2, 3)
>>> sum(T)
6
>>> any(T)
True
>>> all(T)
True
>>> 
>>> # ------------------- zip()
>>> 
>>> T1 = ('anil', 'sunil
      
SyntaxError: EOL while scanning string literal
>>> , 'raj')
SyntaxError: invalid syntax
>>> T1 = ('anil', 'sunil', 'raj')
>>> T2 = ('bangalore', 'chennai', 'hyderabad')
>>> zip(T1, T2)
<zip object at 0x0000022E9AD4A048>
>>> list(zip(T1, T2))
[('anil', 'bangalore'), ('sunil', 'chennai'), ('raj', 'hyderabad')]
>>> dict(zip(T1, T2))
{'anil': 'bangalore', 'sunil': 'chennai', 'raj': 'hyderabad'}
>>> 
>>> 
>>> 
>>> L = [('anil', 'bangalore'), ('sunil', 'chennai'), ('raj', 'hyderabad')]
>>> list(zip(*L))
[('anil', 'sunil', 'raj'), ('bangalore', 'chennai', 'hyderabad')]
>>> 
>>> # zipping, unzipping
>>> 
>>> 
>>> # ----------------------------- unpacking -> lists/tuples
>>> 
>>> T
(1, 2, 3)
>>> L
[('anil', 'bangalore'), ('sunil', 'chennai'), ('raj', 'hyderabad')]
>>> 
>>> 
>>> L = ["red", "green", "blue"]
>>> r, g, b = L
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> 
>>> L = ["red", "green", "blue", "yellow", "goldenm"]
>>> r, g, b = L
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    r, g, b = L
ValueError: too many values to unpack (expected 3)
>>> 
>>> 
>>> r, g, b, *x = L
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> x
['yellow', 'goldenm']
>>> 
