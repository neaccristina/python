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
>>> try:
	total = sum(int(arg) for arg in sys.argv[1:])
	print ('sum=',total)
except ValueError:
	print('Please supply integer arguments')

	
sum= 0
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
>>> #sys.argv[0] name of the path?
>>> sys.argv[1:]
[]
>>> int(sys.argv[1:])
'''Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    int(sys.argv[1:])
TypeError: int() argument must be a string, a bytes-like object or a number,
not 'list'
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

```
