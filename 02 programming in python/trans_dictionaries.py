Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # ---------------- DICTIONARIES
>>> 
>>> L = ['Raj', 30, 'Deloitte', 'India']
>>> D = {'name':'Raj', 'age':30, 'company':'Deloitte', 'country':'India'}
>>> type(D)
<class 'dict'>
>>> D['name']
'Raj'
>>> D['age']
30
>>> D['country']
'India'
>>> D['company']
'Deloitte'
>>> D['dob'] = '10-12-1982'
>>> D
{'name': 'Raj', 'age': 30, 'company': 'Deloitte', 'country': 'India', 'dob': '10-12-1982'}
>>> D['phone']
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    D['phone']
KeyError: 'phone'
>>> D.pop('age')
30
>>> D
{'name': 'Raj', 'company': 'Deloitte', 'country': 'India', 'dob': '10-12-1982'}
>>> D['name'] = 'Anil'
>>> D
{'name': 'Anil', 'company': 'Deloitte', 'country': 'India', 'dob': '10-12-1982'}
>>> 
>>> 'name' in D
True
>>> D['hobbies'] = ['Cricket', 'Movies']
>>> D
{'name': 'Anil', 'company': 'Deloitte', 'country': 'India', 'dob': '10-12-1982', 'hobbies': ['Cricket', 'Movies']}
>>> 
>>> # ------------------------
>>> 
>>> D.keys()
dict_keys(['name', 'company', 'country', 'dob', 'hobbies'])
>>> D.values()
dict_values(['Anil', 'Deloitte', 'India', '10-12-1982', ['Cricket', 'Movies']])
>>> D.items()
dict_items([('name', 'Anil'), ('company', 'Deloitte'), ('country', 'India'), ('dob', '10-12-1982'), ('hobbies', ['Cricket', 'Movies'])])
>>> 
>>> 
>>> # -----------------------
>>> 
>>> D1 = {'addr':'J P Nagar, Bengaluru', 'vehicles':['bike', 'car']}
>>> D.update(D1)
>>> D
{'name': 'Anil', 'company': 'Deloitte', 'country': 'India', 'dob': '10-12-1982', 'hobbies': ['Cricket', 'Movies'], 'addr': 'J P Nagar, Bengaluru', 'vehicles': ['bike', 'car']}
>>> 
>>> 
>>> for k, v in D.items():
	print(k, ' ---> ', v)

	
name  --->  Anil
company  --->  Deloitte
country  --->  India
dob  --->  10-12-1982
hobbies  --->  ['Cricket', 'Movies']
addr  --->  J P Nagar, Bengaluru
vehicles  --->  ['bike', 'car']
>>> 
>>> 
>>> D['companydetails'] = {'company':'Deloitte', 'ceo':'Punit Renjen', 'manager':'Swetha'}
>>> D
{'name': 'Anil', 'company': 'Deloitte', 'country': 'India', 'dob': '10-12-1982', 'hobbies': ['Cricket', 'Movies'], 'addr': 'J P Nagar, Bengaluru', 'vehicles': ['bike', 'car'], 'companydetails': {'company': 'Deloitte', 'ceo': 'Punit Renjen', 'manager': 'Swetha'}}
>>> D_anil = {'name': 'Anil', 'company': 'Deloitte', 'country': 'India', 'dob': '10-12-1982', 'hobbies': ['Cricket', 'Movies'], 'addr': 'J P Nagar, Bengaluru', 'vehicles': ['bike', 'car'], 'companydetails': {'company': 'Deloitte', 'ceo': 'Punit Renjen', 'manager': 'Swetha'}}
>>> D_sunil = {'name': 'Sunil', 'company': 'Deloitte', 'country': 'India', 'dob': '10-12-1982', 'hobbies': ['Cricket', 'Movies'], 'addr': 'J P Nagar, Bengaluru', 'vehicles': ['bike', 'car'], 'companydetails': {'company': 'Deloitte', 'ceo': 'Punit Renjen', 'manager': 'Swetha'}}
>>> D_raj = {'name': 'Raj', 'company': 'Deloitte', 'country': 'India', 'dob': '10-12-1982', 'hobbies': ['Cricket', 'Movies'], 'addr': 'J P Nagar, Bengaluru', 'vehicles': ['bike', 'car'], 'companydetails': {'company': 'Deloitte', 'ceo': 'Punit Renjen', 'manager': 'Swetha'}}
>>> 
>>> 
>>> 
>>> D_anil
{'name': 'Anil', 'company': 'Deloitte', 'country': 'India', 'dob': '10-12-1982', 'hobbies': ['Cricket', 'Movies'], 'addr': 'J P Nagar, Bengaluru', 'vehicles': ['bike', 'car'], 'companydetails': {'company': 'Deloitte', 'ceo': 'Punit Renjen', 'manager': 'Swetha'}}
>>> D_sunil
{'name': 'Sunil', 'company': 'Deloitte', 'country': 'India', 'dob': '10-12-1982', 'hobbies': ['Cricket', 'Movies'], 'addr': 'J P Nagar, Bengaluru', 'vehicles': ['bike', 'car'], 'companydetails': {'company': 'Deloitte', 'ceo': 'Punit Renjen', 'manager': 'Swetha'}}
>>> D-raj
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    D-raj
NameError: name 'raj' is not defined
>>> D_raj
{'name': 'Raj', 'company': 'Deloitte', 'country': 'India', 'dob': '10-12-1982', 'hobbies': ['Cricket', 'Movies'], 'addr': 'J P Nagar, Bengaluru', 'vehicles': ['bike', 'car'], 'companydetails': {'company': 'Deloitte', 'ceo': 'Punit Renjen', 'manager': 'Swetha'}}
>>> 
>>> 
>>> CD = {'anil':D_anil, 'sunil': D_sunil, 'raj':D_raj }
>>> CD
{'anil': {'name': 'Anil', 'company': 'Deloitte', 'country': 'India', 'dob': '10-12-1982', 'hobbies': ['Cricket', 'Movies'], 'addr': 'J P Nagar, Bengaluru', 'vehicles': ['bike', 'car'], 'companydetails': {'company': 'Deloitte', 'ceo': 'Punit Renjen', 'manager': 'Swetha'}}, 'sunil': {'name': 'Sunil', 'company': 'Deloitte', 'country': 'India', 'dob': '10-12-1982', 'hobbies': ['Cricket', 'Movies'], 'addr': 'J P Nagar, Bengaluru', 'vehicles': ['bike', 'car'], 'companydetails': {'company': 'Deloitte', 'ceo': 'Punit Renjen', 'manager': 'Swetha'}}, 'raj': {'name': 'Raj', 'company': 'Deloitte', 'country': 'India', 'dob': '10-12-1982', 'hobbies': ['Cricket', 'Movies'], 'addr': 'J P Nagar, Bengaluru', 'vehicles': ['bike', 'car'], 'companydetails': {'company': 'Deloitte', 'ceo': 'Punit Renjen', 'manager': 'Swetha'}}}
>>> D['raj']
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    D['raj']
KeyError: 'raj'
>>> CD['raj']
{'name': 'Raj', 'company': 'Deloitte', 'country': 'India', 'dob': '10-12-1982', 'hobbies': ['Cricket', 'Movies'], 'addr': 'J P Nagar, Bengaluru', 'vehicles': ['bike', 'car'], 'companydetails': {'company': 'Deloitte', 'ceo': 'Punit Renjen', 'manager': 'Swetha'}}
>>> CD['raj']['companydetails']['manager']
'Swetha'
>>> CD['raj']['companydetails']['manager'] = 'Chetri Govind'
>>> CD
{'anil': {'name': 'Anil', 'company': 'Deloitte', 'country': 'India', 'dob': '10-12-1982', 'hobbies': ['Cricket', 'Movies'], 'addr': 'J P Nagar, Bengaluru', 'vehicles': ['bike', 'car'], 'companydetails': {'company': 'Deloitte', 'ceo': 'Punit Renjen', 'manager': 'Swetha'}}, 'sunil': {'name': 'Sunil', 'company': 'Deloitte', 'country': 'India', 'dob': '10-12-1982', 'hobbies': ['Cricket', 'Movies'], 'addr': 'J P Nagar, Bengaluru', 'vehicles': ['bike', 'car'], 'companydetails': {'company': 'Deloitte', 'ceo': 'Punit Renjen', 'manager': 'Swetha'}}, 'raj': {'name': 'Raj', 'company': 'Deloitte', 'country': 'India', 'dob': '10-12-1982', 'hobbies': ['Cricket', 'Movies'], 'addr': 'J P Nagar, Bengaluru', 'vehicles': ['bike', 'car'], 'companydetails': {'company': 'Deloitte', 'ceo': 'Punit Renjen', 'manager': 'Chetri Govind'}}}
>>> 
