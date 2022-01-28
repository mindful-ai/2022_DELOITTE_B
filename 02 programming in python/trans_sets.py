Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # ------------------- SETS
>>> 
>>> s = "mississippi"
>>> list(s)
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> tuple(s)
('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
>>> set(s)
{'m', 'i', 's', 'p'}
>>> 
>>> 
>>> s1 = set('abcdefgh')
>>> s1
{'c', 'f', 'd', 'a', 'h', 'g', 'b', 'e'}
>>> s2 = {'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'}
>>> s2
{'f', 'l', 'h', 'g', 'j', 'k', 'e', 'i'}
>>> 
>>> # ---------------------------- operators
>>> 
>>> s1 & s2
{'g', 'f', 'e', 'h'}
>>> s1 | s2
{'c', 'f', 'd', 'a', 'h', 'l', 'g', 'k', 'b', 'i', 'e', 'j'}
>>> s1 ^ s2
{'c', 'l', 'd', 'a', 'j', 'k', 'b', 'i'}
>>> 
>>> # ---------------------------- functions
>>> 
>>> s1
{'c', 'f', 'd', 'a', 'h', 'g', 'b', 'e'}
>>> s1.add('x')
>>> s1
{'c', 'f', 'd', 'a', 'h', 'g', 'b', 'e', 'x'}
>>> s3 = {'y', 'z'}
>>> s1.update(s3)
>>> s1
{'c', 'f', 'd', 'a', 'h', 'z', 'g', 'b', 'e', 'x', 'y'}
>>> 'x' in s1
True
>>> s1.remove('x')
>>> s1
{'c', 'f', 'd', 'a', 'h', 'z', 'g', 'b', 'e', 'y'}
>>> 
>>> 
>>> s1.intersection(s2)
{'g', 'f', 'e', 'h'}
>>> s1.union(s2)
{'c', 'f', 'd', 'a', 'h', 'z', 'l', 'g', 'k', 'b', 'i', 'e', 'y', 'j'}
>>> 
