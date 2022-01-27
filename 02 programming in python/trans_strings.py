Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # ------------------------------ Strings
>>> 
>>> s = "python"
>>> type(s)
<class 'str'>
>>> 
>>> # ----------------------------- immutable concept
>>> 
>>> s
'python'
>>> s[0]
'p'
>>> s[0] = 'X'
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s[0] = 'X'
TypeError: 'str' object does not support item assignment
>>> 
>>> # ----------------------------- subscripts
>>> 
>>> 
>>> s[0]
'p'
>>> s[1]
'y'
>>> s[2]
't'
>>> s[-1]
'n'
>>> s[-2]
'o'
>>> s[-3]
'h'
>>> 
>>> s
'python'
>>> s[1:3]
'yt'
>>> s[1:4]
'yth'
>>> s[-2:-5]
''
>>> s[-5:-2]
'yth'
>>> 
>>> 
>>> s[0:4]
'pyth'
>>> s[:4]
'pyth'
>>> s[3:6]
'hon'
>>> s[3:]
'hon'
>>> s[:]
'python'
>>> 
>>> 
>>> s[1:5]
'ytho'
>>> s = 'computer'
>>> s[1:7]
'ompute'
>>> s[1:7:2]
'opt'
>>> s[::2]
'cmue'
>>> 
>>> 
>>> s[::-1]
'retupmoc'
>>> s[::-2]
'rtpo'
>>> 
>>> s[2:8]
'mputer'
>>> s[2:8:-1]
''
>>> s[2:8][::-1]
'retupm'
>>> 
>>> 
>>> # ------------------------------ operators
>>> 
>>> 'abc' + 'def'
'abcdef'
>>> 
>>> 'abc' * 5
'abcabcabcabcabc'
>>> 
>>> s
'computer'
>>> 'put' in s
True
>>> 'app' in s
False
>>> 
>>> len(s)
8
>>> 
>>> type(s) == str
True
>>> 
>>> isinstance(s, str)
True
>>> isinstance(s, int)
False
>>> 
>>> del s
>>> s
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> 
>>> # ---------------------------------- functions
>>> 
>>> # ----- case of the string
>>> 
>>> s
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> s = "computer"
>>> s.upper()
'COMPUTER'
>>> s
'computer'
>>> s.lower()
'computer'
>>> s.capitalize()
'Computer'
>>> 
>>> 
>>> # --------------- checking
>>> 
>>> 'abc'.isdigit()
False
>>> '123'.isdigit()
True
>>> 'abc'.isalpha()
True
>>> '123sdf'.isalnum()
True
>>> '   '.isspace()
True
>>> 
>>> 
>>> # --------------- searching
>>> 
>>> s
'computer'
>>> s.find('put')
3
>>> s = "mississippi"
>>> s.find('ss')
2
>>> s.rfind('ss)
	
SyntaxError: EOL while scanning string literal
>>> s.rfind('ss')
5
>>> s.count('ss')
2
>>> 'ss' in s
True
>>> 
>>> 
>>> # ------------------ modifications
>>> 
>>> # replacing
>>> ip = '192-168-1-1'
>>> ip.replace('-', '.')
'192.168.1.1'
>>> ip
'192-168-1-1'
>>> newip = ip.replace('-', '.')
>>> newip
'192.168.1.1'
>>> 

>>> # check the begin/end sections of the string
>>> 
>>> site = "www.google.com"
>>> site.beginswith('http')
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    site.beginswith('http')
AttributeError: 'str' object has no attribute 'beginswith'
>>> site.startswith('http')
False
>>> site.endswith('com')
True
>>> 
>>> 
>>> # stripping
>>> 
>>> text = ' 14534556   '
>>> text.strip()
'14534556'
>>> text.lstrip()
'14534556   '
>>> text.rstrip()
' 14534556'
>>> 
>>> 
>>> # justification
>>> 
>>> s
'mississippi'
>>> s.ljust(30)
'mississippi                   '
>>> s.rjust(30, '>')
'>>>>>>>>>>>>>>>>>>>mississippi'
>>> 
>>> 
>>> # split and join
>>> 
>>> text = 'mary had a little lamb'
>>> text.split()
['mary', 'had', 'a', 'little', 'lamb']
>>> text.split('a')
['m', 'ry h', 'd ', ' little l', 'mb']
>>> 
>>> L = ['mary', 'had', 'a', 'little', 'lamb']
>>> type(L)
<class 'list'>
>>> '-'.join(L)
'mary-had-a-little-lamb'
>>> 
