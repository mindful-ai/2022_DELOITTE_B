Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a =10
>>> type(a)
<class 'int'>
>>> b = 10.4
>>> type(b)
<class 'float'>
>>> c = -67.4
>>> type(c)
<class 'float'>
>>> # ----------------------------- Operators
>>> 
>>> # ---- Arithmetic operators
>>> 
>>> a = 10
>>> b = 3
>>> a + b
13
>>> res = a + b
>>> res
13
>>> a - b
7
>>> a * b
30
>>> a / b
3.3333333333333335
>>> a % b
1
>>> a // b
3
>>> a ** b
1000
>>> 
>>> # --------------- Relational operators
>>> 
>>> a > b  # Is a greater than b?
True
>>> a < b
False
>>> a <= b
False
>>> a >= b
True
>>> a == b
False
>>> a != b
True
>>> a == b * 3 + 1
True
>>> 
>>> # ----------------- Logical operators
>>> 
>>> a > b and a >= 10
True
>>> a > b or a < 5
True
>>> a > b and a < 5
False
>>> a > b and not a < 5
True
>>> 
>>> 
>>> # ---------------------------------- in built functions
>>> 
>>> a > b || a < 5
SyntaxError: invalid syntax
>>> # ----- Vishnuvardhan
>>> 
>>> a = 100
>>> b = 56
>>> 
>>> a - b
44
>>> b - a
-44
>>> abs(a - b)
44
>>> abs(b - a)
44
>>> type(a)
<class 'int'>
>>> c = float(a)
>>> type(c)
<class 'float'>
>>> 
>>> 
>>> a
100
>>> hex(a)
'0x64'
>>> oct(a)
'0o144'
>>> bin(a)
'0b1100100'
>>> 
>>> 
>>> s = '1010'
>>> s + 10
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    s + 10
TypeError: can only concatenate str (not "int") to str
>>> type(s)
<class 'str'>
>>> 
>>> 
>>> int(s) + 10
1020
>>> 
>>> 
>>> int(s, 2) + 10
20
>>> 
>>> 
>>> s = '10101010'
>>> int(s, 2)
170
>>> h = '0x69Af'
>>> int(h, 16)
27055
>>> 
>>> bin(h)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    bin(h)
TypeError: 'str' object cannot be interpreted as an integer
>>> bin(int(h, 16))
'0b110100110101111'
>>> 
>>> 
>>> myfunc = lambda h : bin(int(h, 16))
>>> type(myfunc)
<class 'function'>
>>> myfunc('0h67FA')
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    myfunc('0h67FA')
  File "<pyshell#83>", line 1, in <lambda>
    myfunc = lambda h : bin(int(h, 16))
ValueError: invalid literal for int() with base 16: '0h67FA'
>>> myfunc('0x45FA')
'0b100010111111010'
>>> 
>>> 
>>> # --------------------------------- in - built modules
>>> 
>>> a = 90
>>> # find the sine value of a
>>> 
>>> sin(a)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    sin(a)
NameError: name 'sin' is not defined
>>> 
>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> 
>>> sin(a)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    sin(a)
NameError: name 'sin' is not defined
>>> math.sin(a)
0.8939966636005579
>>> math.sin(a * 3.14/180)
0.9999996829318346
>>> math.sin(a * 3.14159/180)
0.9999999999991198
>>> math.sin(a * math.pi/180)
1.0
>>> math.sin(math.radians(a))
1.0
>>> 
