Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # ------------------- inputs
>>> 
>>> input()
34
'34'
>>> a = input("Enter a number:")
Enter a number:56
>>> a
'56'
>>> 
>>> a + 10
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a + 10
TypeError: can only concatenate str (not "int") to str
>>> int(a) + 10
66
>>> b = int(input("Enter a number: "))
Enter a number: 345
>>> b + 100
445
>>> 
>>> 
>>> # ------------------------------ outputs
>>> 
>>> 
>>> name = 'anil'
>>> age = 35
>>> 
>>> print("My name is ", name, " age is ", age)
My name is  anil  age is  35
>>> 
>>> print("My name is %s and age is %d" % (name, age))
My name is anil and age is 35
>>> 
>>> "my name is {} and age is {}".format(name, age)
'my name is anil and age is 35'
>>> "my name is {0} and age is {1}".format(name, age)
'my name is anil and age is 35'
>>> "my name is {1} and age is {0}".format(name, age)
'my name is 35 and age is anil'
>>> "my name is {0:10} and age is {1:5}".format(name, age)
'my name is anil       and age is    35'
>>> "my name is {0:>10} and age is {1:<5}".format(name, age)
'my name is       anil and age is 35   '
>>> "my name is {0:^10} and age is {1:^5}".format(name, age)
'my name is    anil    and age is  35  '
>>> 
>>> 
>>> template = "my name is {0:^10} and age is {1:^5}"
>>> data = [('Anil', 35), ('Sunil', 45), ('Raj', 34)]
>>> for k,v in data:
	print(template.format(k, v))

	
my name is    Anil    and age is  35  
my name is   Sunil    and age is  45  
my name is    Raj     and age is  34  
>>> 
