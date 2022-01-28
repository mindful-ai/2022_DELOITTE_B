Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # --------------------- TEST FILES
>>> 
>>> # TEXT FILE!!
>>> 
>>> # open(), path, modes -> 'w', 'r', 'a', 'b'
>>> # close()
>>> # Reading -> read(), readline(), readlines()
>>> # Cursor/pointer -> tell(), seek()
>>> # Writing -> write(), writelines()
>>> 
>>> path = "C:\Users\Purushotham\Desktop\deloitte\2022\02 programming in python\lyrics.txt"
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> 
>>> path = "c:\new\read\text\a.txt"
>>> print(path)
c:
ewead	ext.txt
>>> path = r"c:\new\read\text\a.txt"
>>> print(path)
c:\new\read\text\a.txt
>>> 
>>> 
>>> path = r"C:\Users\Purushotham\Desktop\deloitte\2022\02 programming in python\lyrics.txt"
>>> 
>>> f = open(path, 'r')
>>> type(f)
<class '_io.TextIOWrapper'>
>>> f
<_io.TextIOWrapper name='C:\\Users\\Purushotham\\Desktop\\deloitte\\2022\\02 programming in python\\lyrics.txt' mode='r' encoding='cp1252'>
>>> 
>>> 
>>> c = f.read()
>>> c
"Do you know what's worth fighting for\nWhen it's not worth dying for?\nDoes it take your breath away\nAnd you feel yourself suffocating?\nDoes the pain weigh out the pride?\nAnd you look for a place to hide\nDid someone break your heart inside?\nYou're in ruins\n\nOne, 21 guns\nLay down your arms and give up the fight\nOne, 21 guns\nThrow up your arms into the sky\nYou and I\n\nWhen you're at the end of the road\nAnd you lost all sense of control\nAnd your thoughts have taken their toll\nWhen your mind breaks the spirit of your soul\nYour faith walks on broken glass\nAnd the hangover doesn't pass\nNothing's ever built to last\nYou're in ruins\n\nOne, 21 guns\nLay down your arms and give up the fight\nOne, 21 guns\nThrow up your arms into the sky\nYou and I\n\nDid you try to live on your own\nWhen you burned down the house and home?\nDid you stand too close to the fire\nLike a liar looking for forgiveness from a stone?\n\nWhen it's time to live and let die\nAnd you can't get another try\nSomething inside this heart has died\nYou're in ruins\n\nOne, 21 guns\nLay down your arms and give up the fight\nOne, 21 guns\nThrow up your arms into the sky\nOne, 21 guns\nLay down your arms and give up the fight\nOne, 21 guns\nThrow up your arms into the sky\nYou and I"
>>> print(c)
Do you know what's worth fighting for
When it's not worth dying for?
Does it take your breath away
And you feel yourself suffocating?
Does the pain weigh out the pride?
And you look for a place to hide
Did someone break your heart inside?
You're in ruins

One, 21 guns
Lay down your arms and give up the fight
One, 21 guns
Throw up your arms into the sky
You and I

When you're at the end of the road
And you lost all sense of control
And your thoughts have taken their toll
When your mind breaks the spirit of your soul
Your faith walks on broken glass
And the hangover doesn't pass
Nothing's ever built to last
You're in ruins

One, 21 guns
Lay down your arms and give up the fight
One, 21 guns
Throw up your arms into the sky
You and I

Did you try to live on your own
When you burned down the house and home?
Did you stand too close to the fire
Like a liar looking for forgiveness from a stone?

When it's time to live and let die
And you can't get another try
Something inside this heart has died
You're in ruins

One, 21 guns
Lay down your arms and give up the fight
One, 21 guns
Throw up your arms into the sky
One, 21 guns
Lay down your arms and give up the fight
One, 21 guns
Throw up your arms into the sky
You and I
>>> c = read()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    c = read()
NameError: name 'read' is not defined
>>> c = f.read()
>>> c
''
>>> c.seek()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    c.seek()
AttributeError: 'str' object has no attribute 'seek'
>>> f.seek()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    f.seek()
TypeError: seek() takes at least 1 argument (0 given)
>>> f.tell()
1274
>>> len(c)
0
>>> c = "Do you know what's worth fighting for\nWhen it's not worth dying for?\nDoes it take your breath away\nAnd you feel yourself suffocating?\nDoes the pain weigh out the pride?\nAnd you look for a place to hide\nDid someone break your heart inside?\nYou're in ruins\n\nOne, 21 guns\nLay down your arms and give up the fight\nOne, 21 guns\nThrow up your arms into the sky\nYou and I\n\nWhen you're at the end of the road\nAnd you lost all sense of control\nAnd your thoughts have taken their toll\nWhen your mind breaks the spirit of your soul\nYour faith walks on broken glass\nAnd the hangover doesn't pass\nNothing's ever built to last\nYou're in ruins\n\nOne, 21 guns\nLay down your arms and give up the fight\nOne, 21 guns\nThrow up your arms into the sky\nYou and I\n\nDid you try to live on your own\nWhen you burned down the house and home?\nDid you stand too close to the fire\nLike a liar looking for forgiveness from a stone?\n\nWhen it's time to live and let die\nAnd you can't get another try\nSomething inside this heart has died\nYou're in ruins\n\nOne, 21 guns\nLay down your arms and give up the fight\nOne, 21 guns\nThrow up your arms into the sky\nOne, 21 guns\nLay down your arms and give up the fight\nOne, 21 guns\nThrow up your arms into the sky\nYou and I"
>>> len(c)
1226
>>> f.seek(0)
0
>>> f.read(10)
'Do you kno'
>>> f.tell()
10
>>> f.read()
"w what's worth fighting for\nWhen it's not worth dying for?\nDoes it take your breath away\nAnd you feel yourself suffocating?\nDoes the pain weigh out the pride?\nAnd you look for a place to hide\nDid someone break your heart inside?\nYou're in ruins\n\nOne, 21 guns\nLay down your arms and give up the fight\nOne, 21 guns\nThrow up your arms into the sky\nYou and I\n\nWhen you're at the end of the road\nAnd you lost all sense of control\nAnd your thoughts have taken their toll\nWhen your mind breaks the spirit of your soul\nYour faith walks on broken glass\nAnd the hangover doesn't pass\nNothing's ever built to last\nYou're in ruins\n\nOne, 21 guns\nLay down your arms and give up the fight\nOne, 21 guns\nThrow up your arms into the sky\nYou and I\n\nDid you try to live on your own\nWhen you burned down the house and home?\nDid you stand too close to the fire\nLike a liar looking for forgiveness from a stone?\n\nWhen it's time to live and let die\nAnd you can't get another try\nSomething inside this heart has died\nYou're in ruins\n\nOne, 21 guns\nLay down your arms and give up the fight\nOne, 21 guns\nThrow up your arms into the sky\nOne, 21 guns\nLay down your arms and give up the fight\nOne, 21 guns\nThrow up your arms into the sky\nYou and I"
>>> 
>>> f.seek(0)
0
>>> f.readline()
"Do you know what's worth fighting for\n"
>>> f.readline()
"When it's not worth dying for?\n"
>>> f.readlines()
['Does it take your breath away\n', 'And you feel yourself suffocating?\n', 'Does the pain weigh out the pride?\n', 'And you look for a place to hide\n', 'Did someone break your heart inside?\n', "You're in ruins\n", '\n', 'One, 21 guns\n', 'Lay down your arms and give up the fight\n', 'One, 21 guns\n', 'Throw up your arms into the sky\n', 'You and I\n', '\n', "When you're at the end of the road\n", 'And you lost all sense of control\n', 'And your thoughts have taken their toll\n', 'When your mind breaks the spirit of your soul\n', 'Your faith walks on broken glass\n', "And the hangover doesn't pass\n", "Nothing's ever built to last\n", "You're in ruins\n", '\n', 'One, 21 guns\n', 'Lay down your arms and give up the fight\n', 'One, 21 guns\n', 'Throw up your arms into the sky\n', 'You and I\n', '\n', 'Did you try to live on your own\n', 'When you burned down the house and home?\n', 'Did you stand too close to the fire\n', 'Like a liar looking for forgiveness from a stone?\n', '\n', "When it's time to live and let die\n", "And you can't get another try\n", 'Something inside this heart has died\n', "You're in ruins\n", '\n', 'One, 21 guns\n', 'Lay down your arms and give up the fight\n', 'One, 21 guns\n', 'Throw up your arms into the sky\n', 'One, 21 guns\n', 'Lay down your arms and give up the fight\n', 'One, 21 guns\n', 'Throw up your arms into the sky\n', 'You and I']
>>> f.close()
>>> 
>>> 
>>> path
'C:\\Users\\Purushotham\\Desktop\\deloitte\\2022\\02 programming in python\\lyrics.txt'
>>> path = r'C:\\Users\\Purushotham\\Desktop\\deloitte\\2022\\02 programming in python\\lyrics2.txt'
>>> 
>>> f.open(path, 'w')
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    f.open(path, 'w')
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
>>> f = open(path, 'w')
>>> f.write("Song Name  : 21 Guns\n")
21
>>> data = ["Band      : Green Day\n", "OST   : Transformers\n", "----------------------------\n"]
>>> f.write(data)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    f.write(data)
TypeError: write() argument must be str, not list
>>> f.writelines(data)
>>> f.close()
>>> 
>>> c
"Do you know what's worth fighting for\nWhen it's not worth dying for?\nDoes it take your breath away\nAnd you feel yourself suffocating?\nDoes the pain weigh out the pride?\nAnd you look for a place to hide\nDid someone break your heart inside?\nYou're in ruins\n\nOne, 21 guns\nLay down your arms and give up the fight\nOne, 21 guns\nThrow up your arms into the sky\nYou and I\n\nWhen you're at the end of the road\nAnd you lost all sense of control\nAnd your thoughts have taken their toll\nWhen your mind breaks the spirit of your soul\nYour faith walks on broken glass\nAnd the hangover doesn't pass\nNothing's ever built to last\nYou're in ruins\n\nOne, 21 guns\nLay down your arms and give up the fight\nOne, 21 guns\nThrow up your arms into the sky\nYou and I\n\nDid you try to live on your own\nWhen you burned down the house and home?\nDid you stand too close to the fire\nLike a liar looking for forgiveness from a stone?\n\nWhen it's time to live and let die\nAnd you can't get another try\nSomething inside this heart has died\nYou're in ruins\n\nOne, 21 guns\nLay down your arms and give up the fight\nOne, 21 guns\nThrow up your arms into the sky\nOne, 21 guns\nLay down your arms and give up the fight\nOne, 21 guns\nThrow up your arms into the sky\nYou and I"
>>> 
>>> f = open(path, 'a')
>>> f.write(c.upper())
1226
>>> f.close()
>>> 
>>> 
>>> # -------------------------- Constructing a word histogram
>>> 
>>> path
'C:\\\\Users\\\\Purushotham\\\\Desktop\\\\deloitte\\\\2022\\\\02 programming in python\\\\lyrics2.txt'
>>> path = r'C:\\Users\\Purushotham\\Desktop\\deloitte\\2022\\02 programming in python\\lyrics.txt'
>>> 
>>> 
>>> f = open(path)
>>> text = f.read()
>>> f.close()
>>> 
>>> text
"Do you know what's worth fighting for\nWhen it's not worth dying for?\nDoes it take your breath away\nAnd you feel yourself suffocating?\nDoes the pain weigh out the pride?\nAnd you look for a place to hide\nDid someone break your heart inside?\nYou're in ruins\n\nOne, 21 guns\nLay down your arms and give up the fight\nOne, 21 guns\nThrow up your arms into the sky\nYou and I\n\nWhen you're at the end of the road\nAnd you lost all sense of control\nAnd your thoughts have taken their toll\nWhen your mind breaks the spirit of your soul\nYour faith walks on broken glass\nAnd the hangover doesn't pass\nNothing's ever built to last\nYou're in ruins\n\nOne, 21 guns\nLay down your arms and give up the fight\nOne, 21 guns\nThrow up your arms into the sky\nYou and I\n\nDid you try to live on your own\nWhen you burned down the house and home?\nDid you stand too close to the fire\nLike a liar looking for forgiveness from a stone?\n\nWhen it's time to live and let die\nAnd you can't get another try\nSomething inside this heart has died\nYou're in ruins\n\nOne, 21 guns\nLay down your arms and give up the fight\nOne, 21 guns\nThrow up your arms into the sky\nOne, 21 guns\nLay down your arms and give up the fight\nOne, 21 guns\nThrow up your arms into the sky\nYou and I"
>>> 
>>> text = text.lower()
>>> removelist = [',', '?']
>>> for ch in removelist:
	text.replace(ch, '')

	
"do you know what's worth fighting for\nwhen it's not worth dying for?\ndoes it take your breath away\nand you feel yourself suffocating?\ndoes the pain weigh out the pride?\nand you look for a place to hide\ndid someone break your heart inside?\nyou're in ruins\n\none 21 guns\nlay down your arms and give up the fight\none 21 guns\nthrow up your arms into the sky\nyou and i\n\nwhen you're at the end of the road\nand you lost all sense of control\nand your thoughts have taken their toll\nwhen your mind breaks the spirit of your soul\nyour faith walks on broken glass\nand the hangover doesn't pass\nnothing's ever built to last\nyou're in ruins\n\none 21 guns\nlay down your arms and give up the fight\none 21 guns\nthrow up your arms into the sky\nyou and i\n\ndid you try to live on your own\nwhen you burned down the house and home?\ndid you stand too close to the fire\nlike a liar looking for forgiveness from a stone?\n\nwhen it's time to live and let die\nand you can't get another try\nsomething inside this heart has died\nyou're in ruins\n\none 21 guns\nlay down your arms and give up the fight\none 21 guns\nthrow up your arms into the sky\none 21 guns\nlay down your arms and give up the fight\none 21 guns\nthrow up your arms into the sky\nyou and i"
"do you know what's worth fighting for\nwhen it's not worth dying for\ndoes it take your breath away\nand you feel yourself suffocating\ndoes the pain weigh out the pride\nand you look for a place to hide\ndid someone break your heart inside\nyou're in ruins\n\none, 21 guns\nlay down your arms and give up the fight\none, 21 guns\nthrow up your arms into the sky\nyou and i\n\nwhen you're at the end of the road\nand you lost all sense of control\nand your thoughts have taken their toll\nwhen your mind breaks the spirit of your soul\nyour faith walks on broken glass\nand the hangover doesn't pass\nnothing's ever built to last\nyou're in ruins\n\none, 21 guns\nlay down your arms and give up the fight\none, 21 guns\nthrow up your arms into the sky\nyou and i\n\ndid you try to live on your own\nwhen you burned down the house and home\ndid you stand too close to the fire\nlike a liar looking for forgiveness from a stone\n\nwhen it's time to live and let die\nand you can't get another try\nsomething inside this heart has died\nyou're in ruins\n\none, 21 guns\nlay down your arms and give up the fight\none, 21 guns\nthrow up your arms into the sky\none, 21 guns\nlay down your arms and give up the fight\none, 21 guns\nthrow up your arms into the sky\nyou and i"
>>> for ch in removelist:
	text = text.replace(ch, '')

	
>>> text
"do you know what's worth fighting for\nwhen it's not worth dying for\ndoes it take your breath away\nand you feel yourself suffocating\ndoes the pain weigh out the pride\nand you look for a place to hide\ndid someone break your heart inside\nyou're in ruins\n\none 21 guns\nlay down your arms and give up the fight\none 21 guns\nthrow up your arms into the sky\nyou and i\n\nwhen you're at the end of the road\nand you lost all sense of control\nand your thoughts have taken their toll\nwhen your mind breaks the spirit of your soul\nyour faith walks on broken glass\nand the hangover doesn't pass\nnothing's ever built to last\nyou're in ruins\n\none 21 guns\nlay down your arms and give up the fight\none 21 guns\nthrow up your arms into the sky\nyou and i\n\ndid you try to live on your own\nwhen you burned down the house and home\ndid you stand too close to the fire\nlike a liar looking for forgiveness from a stone\n\nwhen it's time to live and let die\nand you can't get another try\nsomething inside this heart has died\nyou're in ruins\n\none 21 guns\nlay down your arms and give up the fight\none 21 guns\nthrow up your arms into the sky\none 21 guns\nlay down your arms and give up the fight\none 21 guns\nthrow up your arms into the sky\nyou and i"
>>> words = text.split()
>>> words
['do', 'you', 'know', "what's", 'worth', 'fighting', 'for', 'when', "it's", 'not', 'worth', 'dying', 'for', 'does', 'it', 'take', 'your', 'breath', 'away', 'and', 'you', 'feel', 'yourself', 'suffocating', 'does', 'the', 'pain', 'weigh', 'out', 'the', 'pride', 'and', 'you', 'look', 'for', 'a', 'place', 'to', 'hide', 'did', 'someone', 'break', 'your', 'heart', 'inside', "you're", 'in', 'ruins', 'one', '21', 'guns', 'lay', 'down', 'your', 'arms', 'and', 'give', 'up', 'the', 'fight', 'one', '21', 'guns', 'throw', 'up', 'your', 'arms', 'into', 'the', 'sky', 'you', 'and', 'i', 'when', "you're", 'at', 'the', 'end', 'of', 'the', 'road', 'and', 'you', 'lost', 'all', 'sense', 'of', 'control', 'and', 'your', 'thoughts', 'have', 'taken', 'their', 'toll', 'when', 'your', 'mind', 'breaks', 'the', 'spirit', 'of', 'your', 'soul', 'your', 'faith', 'walks', 'on', 'broken', 'glass', 'and', 'the', 'hangover', "doesn't", 'pass', "nothing's", 'ever', 'built', 'to', 'last', "you're", 'in', 'ruins', 'one', '21', 'guns', 'lay', 'down', 'your', 'arms', 'and', 'give', 'up', 'the', 'fight', 'one', '21', 'guns', 'throw', 'up', 'your', 'arms', 'into', 'the', 'sky', 'you', 'and', 'i', 'did', 'you', 'try', 'to', 'live', 'on', 'your', 'own', 'when', 'you', 'burned', 'down', 'the', 'house', 'and', 'home', 'did', 'you', 'stand', 'too', 'close', 'to', 'the', 'fire', 'like', 'a', 'liar', 'looking', 'for', 'forgiveness', 'from', 'a', 'stone', 'when', "it's", 'time', 'to', 'live', 'and', 'let', 'die', 'and', 'you', "can't", 'get', 'another', 'try', 'something', 'inside', 'this', 'heart', 'has', 'died', "you're", 'in', 'ruins', 'one', '21', 'guns', 'lay', 'down', 'your', 'arms', 'and', 'give', 'up', 'the', 'fight', 'one', '21', 'guns', 'throw', 'up', 'your', 'arms', 'into', 'the', 'sky', 'one', '21', 'guns', 'lay', 'down', 'your', 'arms', 'and', 'give', 'up', 'the', 'fight', 'one', '21', 'guns', 'throw', 'up', 'your', 'arms', 'into', 'the', 'sky', 'you', 'and', 'i']
>>> 
>>> D = {}
>>> for word in words:
	if word in D.keys():
		D[word] = D[word] + 1
	else:
		D[word] = 1

		
>>> D
{'do': 1, 'you': 11, 'know': 1, "what's": 1, 'worth': 2, 'fighting': 1, 'for': 4, 'when': 5, "it's": 2, 'not': 1, 'dying': 1, 'does': 2, 'it': 1, 'take': 1, 'your': 15, 'breath': 1, 'away': 1, 'and': 15, 'feel': 1, 'yourself': 1, 'suffocating': 1, 'the': 16, 'pain': 1, 'weigh': 1, 'out': 1, 'pride': 1, 'look': 1, 'a': 3, 'place': 1, 'to': 5, 'hide': 1, 'did': 3, 'someone': 1, 'break': 1, 'heart': 2, 'inside': 2, "you're": 4, 'in': 3, 'ruins': 3, 'one': 8, '21': 8, 'guns': 8, 'lay': 4, 'down': 5, 'arms': 8, 'give': 4, 'up': 8, 'fight': 4, 'throw': 4, 'into': 4, 'sky': 4, 'i': 3, 'at': 1, 'end': 1, 'of': 3, 'road': 1, 'lost': 1, 'all': 1, 'sense': 1, 'control': 1, 'thoughts': 1, 'have': 1, 'taken': 1, 'their': 1, 'toll': 1, 'mind': 1, 'breaks': 1, 'spirit': 1, 'soul': 1, 'faith': 1, 'walks': 1, 'on': 2, 'broken': 1, 'glass': 1, 'hangover': 1, "doesn't": 1, 'pass': 1, "nothing's": 1, 'ever': 1, 'built': 1, 'last': 1, 'try': 2, 'live': 2, 'own': 1, 'burned': 1, 'house': 1, 'home': 1, 'stand': 1, 'too': 1, 'close': 1, 'fire': 1, 'like': 1, 'liar': 1, 'looking': 1, 'forgiveness': 1, 'from': 1, 'stone': 1, 'time': 1, 'let': 1, 'die': 1, "can't": 1, 'get': 1, 'another': 1, 'something': 1, 'this': 1, 'has': 1, 'died': 1}
>>> 
>>> f = open('hist.txt')
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    f = open('hist.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'hist.txt'
>>> f = open('hist.txt', 'w')
>>> for key in D.keys().sort():
	f.write(key.rjust(12) + '|' + D[key] + '\n')

	
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    for key in D.keys().sort():
AttributeError: 'dict_keys' object has no attribute 'sort'
>>> for key in sorted(D.keys()):
	f.write(key.rjust(12) + '|' + D[key] + '\n')

	
Traceback (most recent call last):
  File "<pyshell#105>", line 2, in <module>
    f.write(key.rjust(12) + '|' + D[key] + '\n')
TypeError: can only concatenate str (not "int") to str
>>> for key in sorted(D.keys()):
	f.write(key.rjust(12) + '|' + str(D[key]) + '\n')

	
15
15
15
16
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
16
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
16
15
16
15
>>> f.close()
>>> import os
>>> os.getcwd()
'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37'
>>> os.listdir()
['cx_Oracle-doc', 'data.db.bak', 'data.db.dat', 'data.db.dir', 'DLLs', 'Doc', 'examples', 'example_copy.xlsx', 'hist.txt', 'include', 'Lib', 'libs', 'LICENSE.txt', 'man', 'newly_written.xlsx', 'NEWS.txt', 'python.exe', 'python3.dll', 'python37.dll', 'pythonw.exe', 'Scripts', 'share', 'tcl', 'Tools', 'vcruntime140.dll', 'xgboost']
>>> import shutil
>>> shutil.move('hist.txt', r'C:\Users\Purushotham\Desktop\deloitte\2022\02 programming in python')
'C:\\Users\\Purushotham\\Desktop\\deloitte\\2022\\02 programming in python\\hist.txt'
>>> 
