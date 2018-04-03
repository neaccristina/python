```python

######################################
#####  Operational and learning  #####
######################################


#1 line: Output 
>>> print ('Hello, world!')
Hello, world!

#2 lines: Input, assignment 
>>> name=raw_input('What is your name?\n')
'''
NameError                                 Traceback (most recent call last)
<ipython-input-2-e80e5cfc87f7> in <module>()
----> 1 name=raw_input('What is your name?\n')

NameError: name 'raw_input' is not defined
'''

>>> name=input('What is you name?\n')

What is you name?
Cristina

>>> print('Hi, %s.'%name)
Hi, Cristina.

#3 lines: For loop, built-in enumerate function, new style formatting
>>> friends=['john','pat','gary','michael']

>>> for i, name in enumerate(friends):
        print ('iteration {iteration} is {name}'.format(iteration=i,name=name))
        
iteration 0 is john
iteration 1 is pat
iteration 2 is gary
iteration 3 is michael

>>> enumerate(friends)
<enumerate at 0x433fea0>

>>> list(enumerate(friends))
(0, 'john'), (1, 'pat'), (2, 'gary'), (3, 'michael')]

>>> for i,name in enumerate(friends,2):    #sequence that starts at 2
            print(i,name)
    
2 john
3 pat
4 gary
5 michael


>>> for a,b in enumerate(friends,'a'):
    print(a,b)
    
'''
TypeError                                 Traceback (most recent call last)
<ipython-input-12-7aa442ea7299> in <module>()
----> 1 for a,b in enumerate(friends,'a'):
      2     print(a,b)
      3 

TypeError: 'str' object cannot be interpreted as an integer
'''


#4 lines: Fibonacci, tuple assignment 
>>> parents,babies=(1,1)

>>> while babies<100:
      print('this generation has {0} babies'.format(babies))  
      parents,babies=(babies,parents+babies)
  
this generation has 1 babies
this generation has 2 babies
this generation has 3 babies
this generation has 5 babies
this generation has 8 babies
this generation has 13 babies
this generation has 21 babies
this generation has 34 babies
this generation has 55 babies
this generation has 89 babies


>>> def greet_me(**kargs):            #keyworder,variable lenght variable
        for key,value in kargs.items():
            print("{0} = {1}".format(key, value))
        

>>> greet_me(blabla="cristina")
blabla = cristina



#5 lines: Functions 
>>> def greet(name):
        print('Hello',name)
    

>>> greet('cristina')
Hello cristina


#6 lines: Import, regular expressions
>>> import re

>>> for test_string in ['555-1212','ILL-EGAL']:
        if re.match(r'^\d{3}-\d{4}$',test_string):
            print (test_string,'is a valid US local phone number')
        else:    
            print (test_string,'rejected')
        
555-1212 is a valid US local phone number
ILL-EGAL rejected

>>> #string prefixed with r doesn't handle \ in any special way
>>> print('this is a \n test')
this is a 
 test
>>> print(r'this is a \n test')
this is a \n test
>>> #^matches the begging of the string &matches the end
>>> #d{3} matches 3 digits
>>> #re.match returns None is no pos in the string matches the pattern
>>> re.sub(r'[a-zA-Z_][a-zA-Z_0-9]','','jhrhaw%$hg&%^$$@)><:sdfhs')
'%$&%^$$@)><:s'
>>> re.sub(r'[^a-zA-Z_][^a-zA-Z_0-9]','','jhrhaw%$hg&%^$$@)><:sdfhs')
'jhrhawhgsdfhs'

#7 lines: Dictionaries, generator expressions
>>> prices = {'apple': 0.40, 'banana': 0.50}

>>> my_purchase={
    'apple':1,
    'banana':6}

>>> grocery_bill=sum(prices[fruit]*my_purchase[fruit]
    for fruit in my_purchase)

>>> print 'I owe the grocer $%.2f'%grocery_bill
'''File "<ipython-input-29-83eaa9b62578>", line 1
    print 'I owe the grocer $%.2f'%grocery_bill
                                 ^
SyntaxError: invalid syntax
'''

>>> print ('I owe the grocer $%.2f'%grocery_bill)
I owe the grocer $3.40
>>> #%symbol for variable ; .2f->format the value as a no with 2 decimal places
>>> #%grocery_bill -> variable to be substituted in the string



>>> #8 lines: Command line arguments, exception handling
>>> # This program adds up integers in the command line
>>> import sys

>>> sys.argv[1]
'''Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    sys.argv[1]
IndexError: list index out of range
'''

>>> sys.argv[1:]
[]
>>> sys.argv[0]
''
>>> #cl arg passed to a python scritp-runned from inerpreter it returns an empty list

#logs from terminal
'''
PS H:\config\Desktop> python .\test_args.py
sum= 0
PS H:\config\Desktop> python .\test_args.py -c sdfsdfsdf
Please supply integer arguments
PS H:\config\Desktop> python .\test_args.py  1 2
sum= 3
PS H:\config\Desktop> python .\test_args.py  1  5
sum= 6
PS H:\config\Desktop> python .\test_args.py  1  5 10 47 5
sum= 68
PS H:\config\Desktop>
'''

>>> while True:
	try:
		x = int(input("Please enter a number: "))
		break
	except ValueError:
		print("Oops!  That was no valid number.  Try again...")

		
Please enter a number: ff
Oops!  That was no valid number.  Try again...
Please enter a number: kjkj
Oops!  That was no valid number.  Try again...
Please enter a number: 12

>>> def testthis():
	x=1/0

	
>>> try:
	testthis()
except ZeroDivisionError as err:
	print('Handling run-time error:', err)

	
Handling run-time error: division by zero


>>> raise ValueError()
'''Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    raise ValueError()
ValueError
'''
>>> raise NameError('HiThere')
'''Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    raise NameError('HiThere')
NameError: HiThere
'''

>>> #finally clause-> is always executed before leaving the try statement even if an exception occured or not
>>> try:
	raise KeyboardInterrupt
finally:
	print('something')

	
something
Traceback (most recent call last):
  File "<pyshell#173>", line 2, in <module>
    raise KeyboardInterrupt
KeyboardInterrupt
>>> 



>>> #9 lines: Opening files
>>> import glob
>>> glob.glob('*.gif')
[]
>>> glob.glob('*.txt')
['input.txt', 'LICENSE.txt', 'NEWS.txt']
>>> #so glob look in the path name of were you py app resides
>>> import os
>>> os.chdir('C:\\Users\\criss\\Desktop')
>>> os.getcwd()
'C:\\Users\\criss\\Desktop'
>>> glo.glob('*.txt')
'''Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    glo.glob('*.txt')
NameError: name 'glo' is not defined
'''
>>> glob.glob('*.txt')
['anunt.txt', 'assignement.txt', 'assignment.txt', 'final assig.txt', 'finassig.txt', 'hp.txt', 'input.txt', 'issues_encountered.txt', 'listcomprehension.txt', 'python.txt', 'ultimapy.txt', 'video.txt']
>>> # glob supports Unix style pathname extensions
>>> python_files = glob.glob('*.py')
>>> for file_name in sorted(python_files):
	print('    ------') + file_name

	
    ------
'''Traceback (most recent call last):
  File "<pyshell#190>", line 2, in <module>
    print('    ------') + file_name
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
'''
>>> python_files
['29032018.py', 'finassig.py', 'hello.py']
>>> for file_name in sorted(python_files):
	print('    ------', file_name)

	
    ------ 29032018.py
    ------ finassig.py
    ------ hello.py
>>> with open(file_name) as f:
	for line in f:
		print('    ',line.rstrip())

		
     # file: hello.py
     print("Hello world!")
>>> python_files
['29032018.py', 'finassig.py', 'hello.py']
>>> python_files=glob.glob('*.py')
>>> python_files
['hello.py', 'test.py']
>>> for file_name in sorted(python_files):
	print('    ------', file_name)
	with open(file_name) as f:
		for line in f:
			print('    ',line.rstrip())

			
    ------ hello.py
     # file: hello.py
     print("Hello world!")
    ------ test.py
     # file: test.py
     print("Hello world!")
     #this is a test tes
     #check content


>>> #10 lines: Time, conditionals, from..import, for..else
>>> from time import localtime
>>> #define your dictionary
>>> activities={8:'Sleeping',}
>>> activities
{8: 'Sleeping'}
>>> activities={8:'Sleeping',9: 'Commuting',17: 'Working',18: 'Commuting',20: 'Eating',22: 'Resting'}
>>> activities
{8: 'Sleeping', 9: 'Commuting', 17: 'Working', 18: 'Commuting', 20: 'Eating', 22: 'Resting'}
>>> time_now=localtime()
>>> time_now
time.struct_time(tm_year=2018, tm_mon=4, tm_mday=1, tm_hour=17, tm_min=8, tm_sec=25, tm_wday=6, tm_yday=91, tm_isdst=1)
>>> hour=time_now.tm_hour
>>> hour
17
>>> for activity_time in sorted(activities.keys()):
	if hour<activity_time:
		print(activities[activity_time])
		break
	else:
		print('Unknown,afk or sleeping I wish')

		
Unknown,afk or sleeping I wish
Unknown,afk or sleeping I wish
Unknown,afk or sleeping I wish
Commuting
>>> sorted(activities.keys())
[8, 9, 17, 18, 20, 22]



>>> #11 lines: Triple-quoted strings, while loop
>>> REFRAIN = '''
%d bottles of beer on the wall,
%d bottles of beer,
take one down, pass it around,
%d bottles of beer on the wall!
'''
>>> #best exercise ever
>>> bottles_of_beer=99
>>> while bottles_of_beer>1:
	print REFRAIN % (bottles_of_beer, bottles_of_beer,bottles_of_beer-1)

SyntaxError: invalid syntax

>>> while bottles_of_beer>1:
	print (REFRAIN % (bottles_of_beer, bottles_of_beer,bottles_of_beer-1))
	bottles_of_beer-=1

	

99 bottles of beer on the wall,
99 bottles of beer,
take one down, pass it around,
98 bottles of beer on the wall!


98 bottles of beer on the wall,
98 bottles of beer,
take one down, pass it around,
97 bottles of beer on the wall!


97 bottles of beer on the wall,
97 bottles of beer,
take one down, pass it around,
96 bottles of beer on the wall!


96 bottles of beer on the wall,
96 bottles of beer,
take one down, pass it around,
95 bottles of beer on the wall!


95 bottles of beer on the wall,
95 bottles of beer,
take one down, pass it around,
94 bottles of beer on the wall!


94 bottles of beer on the wall,
94 bottles of beer,
take one down, pass it around,
93 bottles of beer on the wall!


93 bottles of beer on the wall,
93 bottles of beer,
take one down, pass it around,
92 bottles of beer on the wall!


92 bottles of beer on the wall,
92 bottles of beer,
take one down, pass it around,
91 bottles of beer on the wall!


91 bottles of beer on the wall,
91 bottles of beer,
take one down, pass it around,
90 bottles of beer on the wall!


90 bottles of beer on the wall,
90 bottles of beer,
take one down, pass it around,
89 bottles of beer on the wall!


89 bottles of beer on the wall,
89 bottles of beer,
take one down, pass it around,
88 bottles of beer on the wall!


88 bottles of beer on the wall,
88 bottles of beer,
take one down, pass it around,
87 bottles of beer on the wall!


87 bottles of beer on the wall,
87 bottles of beer,
take one down, pass it around,
86 bottles of beer on the wall!


86 bottles of beer on the wall,
86 bottles of beer,
take one down, pass it around,
85 bottles of beer on the wall!


85 bottles of beer on the wall,
85 bottles of beer,
take one down, pass it around,
84 bottles of beer on the wall!


84 bottles of beer on the wall,
84 bottles of beer,
take one down, pass it around,
83 bottles of beer on the wall!


83 bottles of beer on the wall,
83 bottles of beer,
take one down, pass it around,
82 bottles of beer on the wall!


82 bottles of beer on the wall,
82 bottles of beer,
take one down, pass it around,
81 bottles of beer on the wall!


81 bottles of beer on the wall,
81 bottles of beer,
take one down, pass it around,
80 bottles of beer on the wall!


80 bottles of beer on the wall,
80 bottles of beer,
take one down, pass it around,
79 bottles of beer on the wall!


79 bottles of beer on the wall,
79 bottles of beer,
take one down, pass it around,
78 bottles of beer on the wall!


78 bottles of beer on the wall,
78 bottles of beer,
take one down, pass it around,
77 bottles of beer on the wall!


77 bottles of beer on the wall,
77 bottles of beer,
take one down, pass it around,
76 bottles of beer on the wall!


76 bottles of beer on the wall,
76 bottles of beer,
take one down, pass it around,
75 bottles of beer on the wall!


75 bottles of beer on the wall,
75 bottles of beer,
take one down, pass it around,
74 bottles of beer on the wall!


74 bottles of beer on the wall,
74 bottles of beer,
take one down, pass it around,
73 bottles of beer on the wall!


73 bottles of beer on the wall,
73 bottles of beer,
take one down, pass it around,
72 bottles of beer on the wall!


72 bottles of beer on the wall,
72 bottles of beer,
take one down, pass it around,
71 bottles of beer on the wall!


71 bottles of beer on the wall,
71 bottles of beer,
take one down, pass it around,
70 bottles of beer on the wall!


70 bottles of beer on the wall,
70 bottles of beer,
take one down, pass it around,
69 bottles of beer on the wall!


69 bottles of beer on the wall,
69 bottles of beer,
take one down, pass it around,
68 bottles of beer on the wall!


68 bottles of beer on the wall,
68 bottles of beer,
take one down, pass it around,
67 bottles of beer on the wall!


67 bottles of beer on the wall,
67 bottles of beer,
take one down, pass it around,
66 bottles of beer on the wall!


66 bottles of beer on the wall,
66 bottles of beer,
take one down, pass it around,
65 bottles of beer on the wall!


65 bottles of beer on the wall,
65 bottles of beer,
take one down, pass it around,
64 bottles of beer on the wall!


64 bottles of beer on the wall,
64 bottles of beer,
take one down, pass it around,
63 bottles of beer on the wall!


63 bottles of beer on the wall,
63 bottles of beer,
take one down, pass it around,
62 bottles of beer on the wall!


62 bottles of beer on the wall,
62 bottles of beer,
take one down, pass it around,
61 bottles of beer on the wall!


61 bottles of beer on the wall,
61 bottles of beer,
take one down, pass it around,
60 bottles of beer on the wall!


60 bottles of beer on the wall,
60 bottles of beer,
take one down, pass it around,
59 bottles of beer on the wall!


59 bottles of beer on the wall,
59 bottles of beer,
take one down, pass it around,
58 bottles of beer on the wall!


58 bottles of beer on the wall,
58 bottles of beer,
take one down, pass it around,
57 bottles of beer on the wall!


57 bottles of beer on the wall,
57 bottles of beer,
take one down, pass it around,
56 bottles of beer on the wall!


56 bottles of beer on the wall,
56 bottles of beer,
take one down, pass it around,
55 bottles of beer on the wall!


55 bottles of beer on the wall,
55 bottles of beer,
take one down, pass it around,
54 bottles of beer on the wall!


54 bottles of beer on the wall,
54 bottles of beer,
take one down, pass it around,
53 bottles of beer on the wall!


53 bottles of beer on the wall,
53 bottles of beer,
take one down, pass it around,
52 bottles of beer on the wall!


52 bottles of beer on the wall,
52 bottles of beer,
take one down, pass it around,
51 bottles of beer on the wall!


51 bottles of beer on the wall,
51 bottles of beer,
take one down, pass it around,
50 bottles of beer on the wall!


50 bottles of beer on the wall,
50 bottles of beer,
take one down, pass it around,
49 bottles of beer on the wall!


49 bottles of beer on the wall,
49 bottles of beer,
take one down, pass it around,
48 bottles of beer on the wall!


48 bottles of beer on the wall,
48 bottles of beer,
take one down, pass it around,
47 bottles of beer on the wall!


47 bottles of beer on the wall,
47 bottles of beer,
take one down, pass it around,
46 bottles of beer on the wall!


46 bottles of beer on the wall,
46 bottles of beer,
take one down, pass it around,
45 bottles of beer on the wall!


45 bottles of beer on the wall,
45 bottles of beer,
take one down, pass it around,
44 bottles of beer on the wall!


44 bottles of beer on the wall,
44 bottles of beer,
take one down, pass it around,
43 bottles of beer on the wall!


43 bottles of beer on the wall,
43 bottles of beer,
take one down, pass it around,
42 bottles of beer on the wall!


42 bottles of beer on the wall,
42 bottles of beer,
take one down, pass it around,
41 bottles of beer on the wall!


41 bottles of beer on the wall,
41 bottles of beer,
take one down, pass it around,
40 bottles of beer on the wall!


40 bottles of beer on the wall,
40 bottles of beer,
take one down, pass it around,
39 bottles of beer on the wall!


39 bottles of beer on the wall,
39 bottles of beer,
take one down, pass it around,
38 bottles of beer on the wall!


38 bottles of beer on the wall,
38 bottles of beer,
take one down, pass it around,
37 bottles of beer on the wall!


37 bottles of beer on the wall,
37 bottles of beer,
take one down, pass it around,
36 bottles of beer on the wall!


36 bottles of beer on the wall,
36 bottles of beer,
take one down, pass it around,
35 bottles of beer on the wall!


35 bottles of beer on the wall,
35 bottles of beer,
take one down, pass it around,
34 bottles of beer on the wall!


34 bottles of beer on the wall,
34 bottles of beer,
take one down, pass it around,
33 bottles of beer on the wall!


33 bottles of beer on the wall,
33 bottles of beer,
take one down, pass it around,
32 bottles of beer on the wall!


32 bottles of beer on the wall,
32 bottles of beer,
take one down, pass it around,
31 bottles of beer on the wall!


31 bottles of beer on the wall,
31 bottles of beer,
take one down, pass it around,
30 bottles of beer on the wall!


30 bottles of beer on the wall,
30 bottles of beer,
take one down, pass it around,
29 bottles of beer on the wall!


29 bottles of beer on the wall,
29 bottles of beer,
take one down, pass it around,
28 bottles of beer on the wall!


28 bottles of beer on the wall,
28 bottles of beer,
take one down, pass it around,
27 bottles of beer on the wall!


27 bottles of beer on the wall,
27 bottles of beer,
take one down, pass it around,
26 bottles of beer on the wall!


26 bottles of beer on the wall,
26 bottles of beer,
take one down, pass it around,
25 bottles of beer on the wall!


25 bottles of beer on the wall,
25 bottles of beer,
take one down, pass it around,
24 bottles of beer on the wall!


24 bottles of beer on the wall,
24 bottles of beer,
take one down, pass it around,
23 bottles of beer on the wall!


23 bottles of beer on the wall,
23 bottles of beer,
take one down, pass it around,
22 bottles of beer on the wall!


22 bottles of beer on the wall,
22 bottles of beer,
take one down, pass it around,
21 bottles of beer on the wall!


21 bottles of beer on the wall,
21 bottles of beer,
take one down, pass it around,
20 bottles of beer on the wall!


20 bottles of beer on the wall,
20 bottles of beer,
take one down, pass it around,
19 bottles of beer on the wall!


19 bottles of beer on the wall,
19 bottles of beer,
take one down, pass it around,
18 bottles of beer on the wall!


18 bottles of beer on the wall,
18 bottles of beer,
take one down, pass it around,
17 bottles of beer on the wall!


17 bottles of beer on the wall,
17 bottles of beer,
take one down, pass it around,
16 bottles of beer on the wall!


16 bottles of beer on the wall,
16 bottles of beer,
take one down, pass it around,
15 bottles of beer on the wall!


15 bottles of beer on the wall,
15 bottles of beer,
take one down, pass it around,
14 bottles of beer on the wall!


14 bottles of beer on the wall,
14 bottles of beer,
take one down, pass it around,
13 bottles of beer on the wall!


13 bottles of beer on the wall,
13 bottles of beer,
take one down, pass it around,
12 bottles of beer on the wall!


12 bottles of beer on the wall,
12 bottles of beer,
take one down, pass it around,
11 bottles of beer on the wall!


11 bottles of beer on the wall,
11 bottles of beer,
take one down, pass it around,
10 bottles of beer on the wall!


10 bottles of beer on the wall,
10 bottles of beer,
take one down, pass it around,
9 bottles of beer on the wall!


9 bottles of beer on the wall,
9 bottles of beer,
take one down, pass it around,
8 bottles of beer on the wall!


8 bottles of beer on the wall,
8 bottles of beer,
take one down, pass it around,
7 bottles of beer on the wall!


7 bottles of beer on the wall,
7 bottles of beer,
take one down, pass it around,
6 bottles of beer on the wall!


6 bottles of beer on the wall,
6 bottles of beer,
take one down, pass it around,
5 bottles of beer on the wall!


5 bottles of beer on the wall,
5 bottles of beer,
take one down, pass it around,
4 bottles of beer on the wall!


4 bottles of beer on the wall,
4 bottles of beer,
take one down, pass it around,
3 bottles of beer on the wall!


3 bottles of beer on the wall,
3 bottles of beer,
take one down, pass it around,
2 bottles of beer on the wall!


2 bottles of beer on the wall,
2 bottles of beer,
take one down, pass it around,
1 bottles of beer on the wall!





#12 lines: Classes

>>>> class BankAccount(object):#(object)not necessary to be specified explicitly in PYthon3
		def __init__(self,initial_balance=0):
			self.balance=initiall_balance
		def deposit(self,amount):    
			self.balance+=amount
		def withdraw(self,amount):    
			self.balance-=amount
		def overdrawn(self):    
			return self.balance<0
		

>>> my_account=BankAccount(15)
'''
NameError                                 Traceback (most recent call last)
<ipython-input-12-02635cd0fac3> in <module>()
----> 1 my_account=BankAccount(15)

<ipython-input-11-3a204e91c39e> in __init__(self, initial_balance)
      1 class BankAccount(object):#(object)not necessary to be specified explicitly in PYthon3
      2     def __init__(self,initial_balance=0):
----> 3         self.balance=initiall_balance
      4     def deposit(self,amount):
      5         self.balance+=amount

NameError: name 'initiall_balance' is not defined
'''
>>> class BankAccount(object):#(object)not necessary to be specified explicitly in PYthon3
		def __init__(self,initial_balance=0):
			self.balance=initial_balance
		def deposit(self,amount):    
			self.balance+=amount
		def withdraw(self,amount):    
			self.balance-=amount
		def overdrawn(self):    
			return self.balance<0
    

>>> my_account=BankAccount(15)

>>> my_account
Out[15]: <__main__.BankAccount at 0x4622518>

>>> print (my_account)
<__main__.BankAccount object at 0x0000000004622518>

>>> my_account.withdraw(5)

>>> print(my_account.balance)
10


>>> class myclass:
		"""bla bla bla"""
		i=12345
    

>>> x=myclass()

>>> x
<__main__.myclass at 0x46228d0>

>>> class myclass2:
		"""bla bla bla """
		i=12345
		def f(self):
			return 'hello world'
    

>>> x=myclass2

>>> x.i
12345

>>> myclass2.i
12345

>>> def __init__(self):
		self.data=[]
    

>>> x=myclass

>>> x
__main__.myclass

>>> x=myclass()

>>> x
<__main__.myclass at 0x4447c18>

>>> x.i
12345

>>> x.f
'''AttributeError                            Traceback (most recent call last)
<ipython-input-32-13a9b991c3f3> in <module>()
----> 1 x.f

AttributeError: 'myclass' object has no attribute 'f'
'''
>>> x.f()
'''AttributeError                            Traceback (most recent call last)
<ipython-input-33-9cdd69494efb> in <module>()
----> 1 x.f()

AttributeError: 'myclass' object has no attribute 'f'
'''
>>> x.f(self)
'''AttributeError                            Traceback (most recent call last)
<ipython-input-34-85920849e1bf> in <module>()
----> 1 x.f(self)

AttributeError: 'myclass' object has no attribute 'f'
'''
>>> x=myclass2()

>>> x.f
<bound method myclass2.f of <__main__.myclass2 object at 0x0000000004622B00>>

>>> x.f()
'hello world'

>>> class Complex:
		def __init__(self,realpart,imagpart):
			self.r=realpart
			self.i=imagpart
        

>>> x=Complex(3.0,-4.5)

>>> x.r
3.0

>>> x.i
-4.5

>>> class dog:
		kind='canine'   #class variable
		def __init__(self,name):
			self.name=name      #instance variable
        

>>> d=dog('woof')

>>> e=dog('woofwoof')

>>> d.kind
'canine'

>>> e.kind
'canine'

>>> d.name
'woof'

>>> e.name
'woofwoof'

>>> class bag:
		def __init__(self):
			self.data=[]
		def add(self,x):    
			self.data.append(x)
		def addtwice(self,x):    
			self.add(x)
			self.add(x)
        

>>> mybag=bag
>>> mybag=bag(1)
'''TypeError                                 Traceback (most recent call last)
<ipython-input-51-c5ceaff8fa56> in <module>()
----> 1 mybag=bag(1)

TypeError: __init__() takes 1 positional argument but 2 were given
'''

>>> mybag=bag()
>>> data
'''NameError                                 Traceback (most recent call last)
<ipython-input-90-6137cde4893c> in <module>()
----> 1 data

NameError: name 'data' is not defined
'''

>>> mybag.data
[]

>>> mybag.add(10)

>>> mybag.data
[10]


>>> class CurrentAcc:
		def __init__(self,customer_name):
			self.name=customer_name
		def get_customer_name(self):    
			return self.name
    

>>> account_holeder=CurrentAcc

>>> account_holeder("cristina")
<__main__.CurrentAcc at 0x443b7f0>

>>> account_holeder=CurrentAcc("Cristina")

>>> account_holeder
<__main__.CurrentAcc at 0x4622908>

>>> account_holeder.get_customer_name()
'Cristina'


>>> class a:
		def __init__(self):
			self.x='Helllooo mister'
		def method_a(self,name):    
			print(self.x+' '+name)
        

>>> eg=a()

>>> eg
<__main__.a at 0x4648668>

>>> eg.method_a("pussycat")
Helllooo mister pussycat





>>> #13 lines: Unit testing with unittest
# added script in test_median.py
#logs from terminal
'''
PS H:\config\Desktop> python .\test_median.py
  File ".\test_median.py", line 6
    if size%2==1:
    ^
IndentationError: unexpected indent
PS H:\config\Desktop> python .\test_median.py
E
======================================================================
ERROR: testMedian (__main__.TestMedian)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".\test_median.py", line 13, in testMedian
    self.failUnlessEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)
  File ".\test_median.py", line 7, in median
    return copy[(size-1)/2]
TypeError: list indices must be integers, not float

----------------------------------------------------------------------
Ran 1 test in 0.014s

FAILED (errors=1)
PS H:\config\Desktop> python .\test_median.py
E
======================================================================
ERROR: testMedian (__main__.TestMedian)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".\test_median.py", line 13, in testMedian
    self.failUnlessEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)
  File ".\test_median.py", line 7, in median
    return copy[(size-1)/2]
TypeError: list indices must be integers, not float

----------------------------------------------------------------------
Ran 1 test in 0.010s

FAILED (errors=1)
PS H:\config\Desktop> python .\test_median.py
E
======================================================================
ERROR: testMedian (__main__.TestMedian)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".\test_median.py", line 13, in testMedian
    self.failUnlessEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)
  File ".\test_median.py", line 7, in median
    return copy[(size-1)/2]
TypeError: list indices must be integers, not float

----------------------------------------------------------------------
Ran 1 test in 0.012s

FAILED (errors=1)
PS H:\config\Desktop> python .\test_median.py
E
======================================================================
ERROR: testMedian (__main__.TestMedian)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".\test_median.py", line 13, in testMedian
    self.failUnlessEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)
  File ".\test_median.py", line 7, in median
    return copy[(size-1)/2]
TypeError: list indices must be integers, not float

----------------------------------------------------------------------
Ran 1 test in 0.010s

FAILED (errors=1)
PS H:\config\Desktop> python .\test_median.py
9
median: 7
PS H:\config\Desktop> python .\test_median.py
9
.\test_median.py:14: DeprecationWarning: Please use assertEqual instead.
  self.failUnlessEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)
.
----------------------------------------------------------------------
Ran 1 test in 0.009s

OK
PS H:\config\Desktop> python .\test_median.py
.\test_median.py:14: DeprecationWarning: Please use assertEqual instead.
  self.failUnlessEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)
.
----------------------------------------------------------------------
Ran 1 test in 0.008s

OK
PS H:\config\Desktop> python .\test_median.py
PS H:\config\Desktop> python .\test_median.py
.\test_median.py:14: DeprecationWarning: Please use assertEqual instead.
  self.failUnlessEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)
.
----------------------------------------------------------------------
Ran 1 test in 0.008s

OK

'''


>>> #14 lines: Doctest-based testing 
# added script in test_median.py
#logs from terminal
'''
PS H:\config\Desktop> python .\doctest.py
Traceback (most recent call last):
  File ".\doctest.py", line 16, in <module>
    doctest.testmod()
AttributeError: 'module' object has no attribute 'testmod'
PS H:\config\Desktop> python .\doctest.py
Traceback (most recent call last):
  File ".\doctest.py", line 16, in <module>
    dtest.testmod()
AttributeError: 'module' object has no attribute 'testmod'

##had problems because I've name the file the same as the module(confused because when I runned dir(doctest) I saw testmod
#after rename

PS H:\config\Desktop> python .\doctest.py
C:\Program Files\Continuum\Anaconda3\python.exe: can't open file '.\doctest.py': [Errno 2] No such file or directory
PS H:\config\Desktop> python .\doctest1.py

##didn't returned anything so succes
#if i change in the program in the coment field from 7 to 5 in order to force it to fail

PS H:\config\Desktop> python .\doctest1.py
  File ".\doctest1.py", line 15
    doctest.testmod()
                    ^
IndentationError: unindent does not match any outer indentation level
PS H:\config\Desktop> python .\doctest1.py
PS H:\config\Desktop> python .\doctest1.py
**********************************************************************
File ".\doctest1.py", line 3, in __main__.median
Failed example:
    median([2, 9, 9, 7, 9, 2, 4, 5, 8])
Expected:
    5
Got:
    7
**********************************************************************
1 items had failures:
   1 of   1 in __main__.median
***Test Failed*** 1 failures.
PS H:\config\Desktop> 

'''


#15 lines: itertools 
>>> from itertools import groupby

>>> lines='''
	this is the
	first paragraph.


	this is the second.
	'''.splitlines()

>>> lines
['', 'this is the', 'first paragraph.', '', '', 'this is the second.']

>>> # Use itertools.groupby and bool to return groups of

>>> # consecutive lines that either have content or don't.

>>> for has_chars,frags in groupby(lines,bool):
		if has_chars:
			print(' '.join(frags))
        
this is the first paragraph.
this is the second.


#16 lines: csv module, tuple unpacking, cmp() built-in 
# added script in csvmodule.py
#logs from terminal
#file stocks.csv was created  after some changes in the code to translate to python3
'''
PS H:\config\Desktop> python .\csvmodule.py
  File ".\csvmodule.py", line 16
    print '%s is %s (%s%%)' % (name, status, pct)
                          ^
SyntaxError: invalid syntax
PS H:\config\Desktop> python .\csvmodule.py
Traceback (most recent call last):
  File ".\csvmodule.py", line 8, in <module>
    ('CNET', 'CNET Networks, Inc.', 8.62, -0.13, -1.49)
TypeError: 'str' does not support the buffer interface
PS H:\config\Desktop> python .\csvmodule.py
Traceback (most recent call last):
  File ".\csvmodule.py", line 4, in <module>
    writer = csv.writer(open('stocks.csv', 'wt', buffering=0))
ValueError: can't have unbuffered text I/O
PS H:\config\Desktop> python .\csvmodule.py
Traceback (most recent call last):
  File ".\csvmodule.py", line 9, in <module>
    ].encode('utf-8'))
AttributeError: 'list' object has no attribute 'encode'
PS H:\config\Desktop> python .\csvmodule.py
Traceback (most recent call last):
  File ".\csvmodule.py", line 6, in <module>
    ('GOOG', 'Google, Inc.', 505.24, 0.47, 0.09).encode('utf-8'),
AttributeError: 'tuple' object has no attribute 'encode'
PS H:\config\Desktop> python .\csvmodule.py
Traceback (most recent call last):
  File ".\csvmodule.py", line 6, in <module>
    ('GOOG', 'Google, Inc.', 505.24, 0.47, 0.09).encode('utf-8'),
AttributeError: 'tuple' object has no attribute 'encode'
PS H:\config\Desktop> python .\csvmodule.py
PS H:\config\Desktop> python .\csvmodule.py
'''


#18 lines: 8-Queens Problem (recursion) 
# added script in queens.py
#logs from terminal
'''
PS H:\config\Desktop> python .\queens.py
  File ".\queens.py", line 24
    print answer
               ^
SyntaxError: invalid syntax
PS H:\config\Desktop> python .\queens.py
Traceback (most recent call last):
  File ".\queens.py", line 23, in <module>
    for answer in solve(BOARD_SIZE):
  File ".\queens.py", line 17, in solve
    smaller_solutions = solve(n - 1)
  File ".\queens.py", line 17, in solve
    smaller_solutions = solve(n - 1)
  File ".\queens.py", line 17, in solve
    smaller_solutions = solve(n - 1)
  File ".\queens.py", line 17, in solve
    smaller_solutions = solve(n - 1)
  File ".\queens.py", line 17, in solve
    smaller_solutions = solve(n - 1)
  File ".\queens.py", line 17, in solve
    smaller_solutions = solve(n - 1)
  File ".\queens.py", line 17, in solve
    smaller_solutions = solve(n - 1)
  File ".\queens.py", line 20, in solve
    for i in xrange(BOARD_SIZE)
NameError: name 'xrange' is not defined
PS H:\config\Desktop> python .\queens.py
[(1, 4), (2, 2), (3, 7), (4, 3), (5, 6), (6, 8), (7, 5), (8, 1)]
[(1, 5), (2, 2), (3, 4), (4, 7), (5, 3), (6, 8), (7, 6), (8, 1)]
[(1, 3), (2, 5), (3, 2), (4, 8), (5, 6), (6, 4), (7, 7), (8, 1)]
[(1, 3), (2, 6), (3, 4), (4, 2), (5, 8), (6, 5), (7, 7), (8, 1)]
[(1, 5), (2, 7), (3, 1), (4, 3), (5, 8), (6, 6), (7, 4), (8, 2)]
[(1, 4), (2, 6), (3, 8), (4, 3), (5, 1), (6, 7), (7, 5), (8, 2)]
[(1, 3), (2, 6), (3, 8), (4, 1), (5, 4), (6, 7), (7, 5), (8, 2)]
[(1, 5), (2, 3), (3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 2)]
[(1, 5), (2, 7), (3, 4), (4, 1), (5, 3), (6, 8), (7, 6), (8, 2)]
[(1, 4), (2, 1), (3, 5), (4, 8), (5, 6), (6, 3), (7, 7), (8, 2)]
[(1, 3), (2, 6), (3, 4), (4, 1), (5, 8), (6, 5), (7, 7), (8, 2)]
[(1, 4), (2, 7), (3, 5), (4, 3), (5, 1), (6, 6), (7, 8), (8, 2)]
[(1, 6), (2, 4), (3, 2), (4, 8), (5, 5), (6, 7), (7, 1), (8, 3)]
[(1, 6), (2, 4), (3, 7), (4, 1), (5, 8), (6, 2), (7, 5), (8, 3)]
[(1, 1), (2, 7), (3, 4), (4, 6), (5, 8), (6, 2), (7, 5), (8, 3)]
[(1, 6), (2, 8), (3, 2), (4, 4), (5, 1), (6, 7), (7, 5), (8, 3)]
[(1, 6), (2, 2), (3, 7), (4, 1), (5, 4), (6, 8), (7, 5), (8, 3)]
[(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)]
[(1, 5), (2, 8), (3, 4), (4, 1), (5, 7), (6, 2), (7, 6), (8, 3)]
[(1, 4), (2, 8), (3, 1), (4, 5), (5, 7), (6, 2), (7, 6), (8, 3)]
[(1, 2), (2, 7), (3, 5), (4, 8), (5, 1), (6, 4), (7, 6), (8, 3)]
[(1, 1), (2, 7), (3, 5), (4, 8), (5, 2), (6, 4), (7, 6), (8, 3)]
[(1, 2), (2, 5), (3, 7), (4, 4), (5, 1), (6, 8), (7, 6), (8, 3)]
[(1, 4), (2, 2), (3, 7), (4, 5), (5, 1), (6, 8), (7, 6), (8, 3)]
[(1, 5), (2, 7), (3, 1), (4, 4), (5, 2), (6, 8), (7, 6), (8, 3)]
[(1, 6), (2, 4), (3, 1), (4, 5), (5, 8), (6, 2), (7, 7), (8, 3)]
[(1, 5), (2, 1), (3, 4), (4, 6), (5, 8), (6, 2), (7, 7), (8, 3)]
[(1, 5), (2, 2), (3, 6), (4, 1), (5, 7), (6, 4), (7, 8), (8, 3)]
[(1, 6), (2, 3), (3, 7), (4, 2), (5, 8), (6, 5), (7, 1), (8, 4)]
[(1, 2), (2, 7), (3, 3), (4, 6), (5, 8), (6, 5), (7, 1), (8, 4)]
[(1, 7), (2, 3), (3, 1), (4, 6), (5, 8), (6, 5), (7, 2), (8, 4)]
[(1, 5), (2, 1), (3, 8), (4, 6), (5, 3), (6, 7), (7, 2), (8, 4)]
[(1, 1), (2, 5), (3, 8), (4, 6), (5, 3), (6, 7), (7, 2), (8, 4)]
[(1, 3), (2, 6), (3, 8), (4, 1), (5, 5), (6, 7), (7, 2), (8, 4)]
[(1, 6), (2, 3), (3, 1), (4, 7), (5, 5), (6, 8), (7, 2), (8, 4)]
[(1, 7), (2, 5), (3, 3), (4, 1), (5, 6), (6, 8), (7, 2), (8, 4)]
[(1, 7), (2, 3), (3, 8), (4, 2), (5, 5), (6, 1), (7, 6), (8, 4)]
[(1, 5), (2, 3), (3, 1), (4, 7), (5, 2), (6, 8), (7, 6), (8, 4)]
[(1, 2), (2, 5), (3, 7), (4, 1), (5, 3), (6, 8), (7, 6), (8, 4)]
[(1, 3), (2, 6), (3, 2), (4, 5), (5, 8), (6, 1), (7, 7), (8, 4)]
[(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]
[(1, 8), (2, 3), (3, 1), (4, 6), (5, 2), (6, 5), (7, 7), (8, 4)]
[(1, 2), (2, 8), (3, 6), (4, 1), (5, 3), (6, 5), (7, 7), (8, 4)]
[(1, 5), (2, 7), (3, 2), (4, 6), (5, 3), (6, 1), (7, 8), (8, 4)]
[(1, 3), (2, 6), (3, 2), (4, 7), (5, 5), (6, 1), (7, 8), (8, 4)]
[(1, 6), (2, 2), (3, 7), (4, 1), (5, 3), (6, 5), (7, 8), (8, 4)]
[(1, 3), (2, 7), (3, 2), (4, 8), (5, 6), (6, 4), (7, 1), (8, 5)]
[(1, 6), (2, 3), (3, 7), (4, 2), (5, 4), (6, 8), (7, 1), (8, 5)]
[(1, 4), (2, 2), (3, 7), (4, 3), (5, 6), (6, 8), (7, 1), (8, 5)]
[(1, 7), (2, 1), (3, 3), (4, 8), (5, 6), (6, 4), (7, 2), (8, 5)]
[(1, 1), (2, 6), (3, 8), (4, 3), (5, 7), (6, 4), (7, 2), (8, 5)]
[(1, 3), (2, 8), (3, 4), (4, 7), (5, 1), (6, 6), (7, 2), (8, 5)]
[(1, 6), (2, 3), (3, 7), (4, 4), (5, 1), (6, 8), (7, 2), (8, 5)]
[(1, 7), (2, 4), (3, 2), (4, 8), (5, 6), (6, 1), (7, 3), (8, 5)]
[(1, 4), (2, 6), (3, 8), (4, 2), (5, 7), (6, 1), (7, 3), (8, 5)]
[(1, 2), (2, 6), (3, 1), (4, 7), (5, 4), (6, 8), (7, 3), (8, 5)]
[(1, 2), (2, 4), (3, 6), (4, 8), (5, 3), (6, 1), (7, 7), (8, 5)]
[(1, 3), (2, 6), (3, 8), (4, 2), (5, 4), (6, 1), (7, 7), (8, 5)]
[(1, 6), (2, 3), (3, 1), (4, 8), (5, 4), (6, 2), (7, 7), (8, 5)]
[(1, 8), (2, 4), (3, 1), (4, 3), (5, 6), (6, 2), (7, 7), (8, 5)]
[(1, 4), (2, 8), (3, 1), (4, 3), (5, 6), (6, 2), (7, 7), (8, 5)]
[(1, 2), (2, 6), (3, 8), (4, 3), (5, 1), (6, 4), (7, 7), (8, 5)]
[(1, 7), (2, 2), (3, 6), (4, 3), (5, 1), (6, 4), (7, 8), (8, 5)]
[(1, 3), (2, 6), (3, 2), (4, 7), (5, 1), (6, 4), (7, 8), (8, 5)]
[(1, 4), (2, 7), (3, 3), (4, 8), (5, 2), (6, 5), (7, 1), (8, 6)]
[(1, 4), (2, 8), (3, 5), (4, 3), (5, 1), (6, 7), (7, 2), (8, 6)]
[(1, 3), (2, 5), (3, 8), (4, 4), (5, 1), (6, 7), (7, 2), (8, 6)]
[(1, 4), (2, 2), (3, 8), (4, 5), (5, 7), (6, 1), (7, 3), (8, 6)]
[(1, 5), (2, 7), (3, 2), (4, 4), (5, 8), (6, 1), (7, 3), (8, 6)]
[(1, 7), (2, 4), (3, 2), (4, 5), (5, 8), (6, 1), (7, 3), (8, 6)]
[(1, 8), (2, 2), (3, 4), (4, 1), (5, 7), (6, 5), (7, 3), (8, 6)]
[(1, 7), (2, 2), (3, 4), (4, 1), (5, 8), (6, 5), (7, 3), (8, 6)]
[(1, 5), (2, 1), (3, 8), (4, 4), (5, 2), (6, 7), (7, 3), (8, 6)]
[(1, 4), (2, 1), (3, 5), (4, 8), (5, 2), (6, 7), (7, 3), (8, 6)]
[(1, 5), (2, 2), (3, 8), (4, 1), (5, 4), (6, 7), (7, 3), (8, 6)]
[(1, 3), (2, 7), (3, 2), (4, 8), (5, 5), (6, 1), (7, 4), (8, 6)]
[(1, 3), (2, 1), (3, 7), (4, 5), (5, 8), (6, 2), (7, 4), (8, 6)]
[(1, 8), (2, 2), (3, 5), (4, 3), (5, 1), (6, 7), (7, 4), (8, 6)]
[(1, 3), (2, 5), (3, 2), (4, 8), (5, 1), (6, 7), (7, 4), (8, 6)]
[(1, 3), (2, 5), (3, 7), (4, 1), (5, 4), (6, 2), (7, 8), (8, 6)]
[(1, 5), (2, 2), (3, 4), (4, 6), (5, 8), (6, 3), (7, 1), (8, 7)]
[(1, 6), (2, 3), (3, 5), (4, 8), (5, 1), (6, 4), (7, 2), (8, 7)]
[(1, 5), (2, 8), (3, 4), (4, 1), (5, 3), (6, 6), (7, 2), (8, 7)]
[(1, 4), (2, 2), (3, 5), (4, 8), (5, 6), (6, 1), (7, 3), (8, 7)]
[(1, 4), (2, 6), (3, 1), (4, 5), (5, 2), (6, 8), (7, 3), (8, 7)]
[(1, 6), (2, 3), (3, 1), (4, 8), (5, 5), (6, 2), (7, 4), (8, 7)]
[(1, 5), (2, 3), (3, 1), (4, 6), (5, 8), (6, 2), (7, 4), (8, 7)]
[(1, 4), (2, 2), (3, 8), (4, 6), (5, 1), (6, 3), (7, 5), (8, 7)]
[(1, 6), (2, 3), (3, 5), (4, 7), (5, 1), (6, 4), (7, 2), (8, 8)]
[(1, 6), (2, 4), (3, 7), (4, 1), (5, 3), (6, 5), (7, 2), (8, 8)]
[(1, 4), (2, 7), (3, 5), (4, 2), (5, 6), (6, 1), (7, 3), (8, 8)]
[(1, 5), (2, 7), (3, 2), (4, 6), (5, 3), (6, 1), (7, 4), (8, 8)]
'''

#20 lines: Prime numbers sieve w/fancy generators 

>>> import itertools

>>> def iter_primes():
		# an iterator of all numbers between 2 and +infinity
		numbers = itertools.count(2)
		# generate primes forever
		while True:
			# get the first number from the iterator (always a prime)
			prime = numbers.next()
			yield prime
			# this code iteratively builds up a chain of
			# filters...slightly tricky, but ponder it a bit
			numbers = itertools.ifilter(prime.__rmod__, numbers)
        

>>> for p in iter_primes():
		if p > 1000:
			break
		print(p)
    
'''AttributeError                            Traceback (most recent call last)
<ipython-input-200-9ad59975ef99> in <module>()
----> 1 for p in iter_primes():
      2     if p > 1000:
      3         break
      4     print(p)
      5 

<ipython-input-199-6ad4efa641b7> in iter_primes()
      5     while True:
      6         # get the first number from the iterator (always a prime)
----> 7         prime = numbers.next()
      8         yield prime
      9         # this code iteratively builds up a chain of

AttributeError: 'itertools.count' object has no attribute 'next'
'''
>>> #changed from iter.next() to next(iter) due to python2 to 3 translate

>>> def iter_primes():
		# an iterator of all numbers between 2 and +infinity
		numbers = itertools.count(2)
		# generate primes forever
		while True:
			# get the first number from the iterator (always a prime)
			prime = next.(numbers)
			yield prime
			# this code iteratively builds up a chain of
			# filters...slightly tricky, but ponder it a bit
			numbers = itertools.ifilter(prime.__rmod__, numbers)
        
'''  File "<ipython-input-202-0943b0d484f1>", line 7
    prime = next.(numbers)
                 ^
SyntaxError: invalid syntax
'''

>>> def iter_primes():
		# an iterator of all numbers between 2 and +infinity
		numbers = itertools.count(2)
		# generate primes forever
		while True:
			# get the first number from the iterator (always a prime)
			prime = next(numbers)
			yield prime
			# this code iteratively builds up a chain of
			# filters...slightly tricky, but ponder it a bit
			numbers = itertools.ifilter(prime.__rmod__, numbers)
        

>>> for p in iter_primes():
		if p > 1000:
			break
		print(p)
    
2
'''AttributeError                            Traceback (most recent call last)
<ipython-input-204-9ad59975ef99> in <module>()
----> 1 for p in iter_primes():
      2     if p > 1000:
      3         break
      4     print(p)
      5 

<ipython-input-203-580a4fb7c7e7> in iter_primes()
      9         # this code iteratively builds up a chain of
     10         # filters...slightly tricky, but ponder it a bit
---> 11         numbers = itertools.ifilter(prime.__rmod__, numbers)
     12 

AttributeError: 'module' object has no attribute 'ifilter'
'''

#change from itertools.filter to filter() build in function due to python 3 use
>>> def iter_primes():
		# an iterator of all numbers between 2 and +infinity
		numbers = itertools.count(2)
		# generate primes forever
		while True:
			# get the first number from the iterator (always a prime)
			prime = next(numbers)
			yield prime
			# this code iteratively builds up a chain of
			# filters...slightly tricky, but ponder it a bit
			numbers = filter(prime.__rmod__, numbers)
        

>>> for p in iter_primes():
		if p > 1000:
			break
		print(p)
		
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113
127
131
137
139
149
151
157
163
167
173
179
181
191
193
197
199
211
223
227
229
233
239
241
251
257
263
269
271
277
281
283
293
307
311
313
317
331
337
347
349
353
359
367
373
379
383
389
397
401
409
419
421
431
433
439
443
449
457
461
463
467
479
487
491
499
503
509
521
523
541
547
557
563
569
571
577
587
593
599
601
607
613
617
619
631
641
643
647
653
659
661
673
677
683
691
701
709
719
727
733
739
743
751
757
761
769
773
787
797
809
811
821
823
827
829
839
853
857
859
863
877
881
883
887
907
911
919
929
937
941
947
953
967
971
977
983
991
997

#21 lines: XML/HTML parsing (using Python 2.5 or third-party library)

>>> dinner_recipe = '''<html><body><table>
	<tr><th>amt</th><th>unit</th><th>item</th></tr>
	<tr><td>24</td><td>slices</td><td>baguette</td></tr>
	<tr><td>2+</td><td>tbsp</td><td>olive oil</td></tr>
	<tr><td>1</td><td>cup</td><td>tomatoes</td></tr>
	<tr><td>1</td><td>jar</td><td>pesto</td></tr>
	</table></body></html>'''

>>> dinner_recipe
'<html><body><table>\n<tr><th>amt</th><th>unit</th><th>item</th></tr>\n<tr><td>24</td><td>slices</td><td>baguette</td></tr>\n<tr><td>2+</td><td>tbsp</td><td>olive oil</td></tr>\n<tr><td>1</td><td>cup</td><td>tomatoes</td></tr>\n<tr><td>1</td><td>jar</td><td>pesto</td></tr>\n</table></body></html>'

>>> import xml.etree.ElementTree as etree

>>> tree = etree.fromstring(dinner_recipe)

>>> pantry = set(['olive oil', 'pesto'])

>>> for ingredient in tree.getiterator('tr'):
		amt, unit, item = ingredient
		if item.tag == "td" and item.text not in pantry:
			print ("%s: %s %s" % (item.text, amt.text, unit.text))
        
baguette: 24 slices
tomatoes: 1 cup

>>> ##oops you only have olive oil and pesto for your recipe. go buy baguette and tomatoes

>>> #28 lines: 8-Queens Problem (define your own exceptions) 

>>> BOARD_SIZE = 8

>>> class BailOut(Exception):
        pass


>>> def validate(queens):
		left = right = col = queens[-1]
		for r in reversed(queens[:-1]):
			left, right = left-1, right+1
			if r in (left, col, right):
				raise BailOut
			

>>> def add_queen(queens):
		for i in range(BOARD_SIZE):
			test_queens = queens + [i]
			try:
				validate(test_queens)
				if len(test_queens) == BOARD_SIZE:
					return test_queens
				else:
					return add_queen(test_queens)
			except BailOut:    
				pass
		raise BailOut    


>>> queens=add_queen([])

>>> print(queens)
[0, 4, 7, 5, 2, 6, 1, 3]

>>> print ("\n".join(". "*q + "Q " + ". "*(BOARD_SIZE-q-1) for q in queens))
Q . . . . . . . 
. . . . Q . . . 
. . . . . . . Q 
. . . . . Q . . 
. . Q . . . . . 
. . . . . . Q . 
. Q . . . . . . 
. . . Q . . . . 

#33 lines: "Guess the Number" Game (edited

>>> import random

>>> guesses_made = 0

>>> name = raw_input('Hello! What is your name?\n')
'''NameError                                 Traceback (most recent call last)
<ipython-input-227-7a102be42772> in <module>()
----> 1 name = raw_input('Hello! What is your name?\n')

NameError: name 'raw_input' is not defined
'''

>>> name = input('Hello! What is your name?\n')

Hello! What is your name?
cristina

>>> number = random.randint(1, 20)

>>> print ('Well, {0}, I am thinking of a number between 1 and 20.'.format(name))
Well, cristina, I am thinking of a number between 1 and 20.

>>> while guesses_made < 6:
		guess = int(input('Take a guess: '))
		guesses_made += 1
		if guess < number:
			print ('Your guess is too low.')
		if guess > number:    
			print ('Your guess is too low.')
		if guess > number:    
			print ('Your guess is too high.')
		if guess == number:    
			break
	if guess==number:    
		print ('Good job, {0}! You guessed my number in {1} guesses!'.format(name, guesses_made))
	else:    
		print ('Nope. The number I was thinking of was {0}'.format(number))
    

Take a guess: 
'''ValueError                                Traceback (most recent call last)
<ipython-input-231-172b4e8d9f8c> in <module>()
      1 while guesses_made < 6:
----> 2     guess = int(input('Take a guess: '))
      3     guesses_made += 1
      4     if guess < number:
      5         print ('Your guess is too low.')

ValueError: invalid literal for int() with base 10: ''
'''
>>> print ('Well, {0}, I am thinking of a number between 1 and 20.'.format(name))
Well, cristina, I am thinking of a number between 1 and 20.

>>> while guesses_made < 6:
		guess = int(input('Take a guess: '))
		guesses_made += 1
		if guess < number:
			print ('Your guess is too low.')
		if guess > number:    
			print ('Your guess is too low.')
		if guess > number:    
			print ('Your guess is too high.')
		if guess == number:    
			break
	if guess==number:    
		print ('Good job, {0}! You guessed my number in {1} guesses!'.format(name, guesses_made))
	else:    
		print ('Nope. The number I was thinking of was {0}'.format(number))
 
Take a guess: 5
Your guess is too low.

Take a guess: 9
Your guess is too low.

Take a guess: 11
Your guess is too low.

Take a guess: 15
Good job, cristina! You guessed my number in 4 guesses!

```
