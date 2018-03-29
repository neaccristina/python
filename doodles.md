```python
#Sintax testing

>>> print ("test1")
'test1'

>>> print ('test2')
'test2'

#Variables and placeholders testing

>>> name, age = "Cristina", 29

>>> print (name)
'Cristina'

>>> print (age)
29

>>> full_name=last_name="test" 

>>> test3 = 'ghilimele'

>>> print(test3)
'ghilimele'

>>> age1=1

>>> print(age1)
1

>>> age2=2

>>> age1+age2
3

>>> full_name+name
'testCristina'

>>> full_name*3
'testtesttest'

#Splicing

>>> bigsentence ='test bla bla phyton'

>>> bigsentence[:3]
'tes'

>>> bigsentence[:-6]
'test bla bla '

>>> sentence="%s is a string placeholder and %d is an integer one "
>>> senetence
'''Traceback (most recent call last):

  File "<input>", line 1, in <module>

NameError: name 'senetence' is not defined
'''
>>> sentence
'%s is a string placeholder and %d is an integer one '

>>> sentence%["cristina",12]
'''Traceback (most recent call last):

  File "<input>", line 1, in <module>

TypeError: not enough arguments for format string
'''
>>> sentence%["cristina","12"]
'''Traceback (most recent call last):

  File "<input>", line 1, in <module>

TypeError: not enough arguments for format string
'''
>>> sentence%("cristina",12)
'cristina is a string placeholder and 12 is an integer one '

>>> sentence%(12,"cristinareverse")
'''Traceback (most recent call last):

  File "<input>", line 1, in <module>

TypeError: %d format: a number is required, not str
'''

#Lists test
>>> listtry1=["oranges","bananas","apples"]

>>> listtry1
['oranges', 'bananas', 'apples']

>>> listtry1[1]
'bananas'

>>> listtry2=[1,2,"cristina"]

>>> listtry2
[1, 2, 'cristina']

>>> listtry1[0:4]
['oranges', 'bananas', 'apples']

>>> listtry1.append("cheese")

>>> listtry1
['oranges', 'bananas', 'apples', 'cheese']

>>> listtry1.append(listtry2)

>>> listtry1
['oranges', 'bananas', 'apples', 'cheese', [1, 2, 'cristina']]

>>> listtry1[4]
[1, 2, 'cristina']

>>> listtry1[4]="cherry"

>>> listtry1
['oranges', 'bananas', 'apples', 'cheese', 'cherry']

>>> del listtry1[3]

>>> listtry1
['oranges', 'bananas', 'apples', 'cherry']

>>> len(listtry1)
4

>>> listtry1+listtry2
['oranges', 'bananas', 'apples', 'cherry', 1, 2, 'cristina']

>>> max(isttry1)
'''Traceback (most recent call last):

  File "<input>", line 1, in <module>

NameError: name 'isttry1' is not defined
'''

>>> max(listtry1)
'oranges'

>>> listnumeri=[1,2,4,67,8]

>>> max(listnumeri)
67

>>> min(istnumeri)
'''Traceback (most recent call last):

  File "<input>", line 1, in <module>

NameError: name 'istnumeri' is not defined
'''
>>> min(listnumeri)
1

>>> 7**3
343


#Test lists

>>> list1 =['a','b', 'c',1, 2, 4, 'd']

>>> list1[:9]
['a', 'b', 'c', 1, 2, 4, 'd']

>>> list1[-6]
'b'

>>> list1[3:5]
[1, 2]

>>> list1[3:6]=[]

>>> list1
['a', 'b', 'c', 'd']

>>> list1[:]
['a', 'b', 'c', 'd']

>>> list1.append(23)

>>> list1
['a', 'b', 'c', 'd', 23]

>>> list1[-1]='e'

>>> list1
['a', 'b', 'c', 'd', 'e']

>>> my_string ="I like bla bla bla"
>>> print len(my_string)
18
>>> print my_string.upper()
I LIKE BLA BLA BLA

>>> family = {'Dad':36, 'cat':35, 'dog':10}
>>> family['Mom'] = 8              
>>> family
{'Dad': 36, 'Mom': 8, 'cat': 35, 'dog': 10} 
>>> family['cat'] = 36            
>>> family
{'Dad': 36, 'Mom': 8, 'cat': 36, 'dog': 10} 

>>> family.keys()        
['Dad', 'Mom', 'cat', 'dog']
>>> family.values()      
[36, 8, 35, 10]

>>> family.items()        
[('Dad', 36), ('Mom', 8), ('cat', 35), ('dog', 10)]

#Fibonacci try
>>> a,b=0,1
>>> while b<10
'''SyntaxError: invalid syntax'''

>>> while b<10:
	print(b)
	a,b=b,a+b
	

1

1

2

3

5

8

#try2
>>> a,b=0,1
>>> while b<1000:
	print(b, end=',')
	a,b=b,a+b
	

1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,

#if try
>>> x=53
>>> if x<0:
	print('less than zero')
elif x==0:
	print('this is zero')
else x>0:

'''SyntaxError: invalid syntax'''

>>> x=53
>>> if x<0:
	print('less than zero')
elif x==0:
	print('this is zero')
elif x>0:
	print('bigger than zero')
else :
	print('yuhu')	

bigger than zero

#for statement

>>> home =['family','cat','dog']
>>> for i in home:
	if home[1]='cat':
'''SyntaxError: invalid syntax'''

>>> for i in home:
	if home[1]=='cat':
		print('she hates the dog')

she hates the dog

she hates the dog

she hates the dog


# for statement

>>> home =['cat','dog','family']
>>> for i in home[:]:
	if len(i)>3:
		home.insert(1,i)		

>>> home
['cat', 'family', 'dog', 'family']

>>> for i in home:
	if len(i)==3:
		print('this is a good pet')
		

this is a good pet

this is a good pet

>>> home
['cat', 'family', 'dog', 'family']

>>> for i in home:
	if len(i)>3:
		home.insert(1,i)		
'''Traceback (most recent call last):

  File "<pyshell#25>", line 3, in <module>

    home.insert(1,i)
'''
KeyboardInterrupt


>>> for i in range(10):
	print(i)	

0

1

2

3

4

5

6

7

8

9

>>> home=['cat','dog','family']
>>> for i in range(len(home)):
	print (i,home[i])	

0 cat

1 dog

2 family



>>> for n in range(2,10):
	print(n)	

2

3

4

5

6

7

8

9



>>> for x in range(2,5):
	print(x)
	

2

3

4



#break and continue

>>> for i in range(2,10):
	if i%2==0:
		print(i,' is an even number')
		continue
	print(i,' is not an even one')	

2  is an even number

3  is not an even one

4  is an even number

5  is not an even one

6  is an even number

7  is not an even one

8  is an even number

9  is not an even one


>>> for i in range(2,10):
	if i%2==0:
		print(i,' is an even number')
		break
	print('something else')	

2  is an even number


>>> for i in range(2,10):
	if i%2==0:
		print('cdfd')
		break

cdfd

>>> for letter in 'Python':
	if letter=='h':
		print(letter)		

h

>>> for letter in 'Python':
	if letter=='h':
		break
	print (letter)


P

y

t

>>> for letter in 'Python':
	if letter=='h':
		continue
	print(letter)	

P

y

t

o

n

>>> for letter in 'Python':
	if letter=='h':
		pass
	print('this is pass')
	print(letter)



>>> import time;

>>> trytime=time.time()

>>> trytime
1522049311.8951094


>>> trytimelocal=time.localtime(time.time())

>>> trytimelocal
time.struct_time(tm_year=2018, tm_mon=3, tm_mday=26, tm_hour=10, tm_min=30, tm_sec=11, tm_wday=0, tm_yday=85, tm_isdst=1)

>>> from datetime import datetime
>>> now = datetime.now()
>>> print '%02d-%02d-%04d' % (now.month, now.day, now.year)
03-26-2018

>>> import calendar

>>> cal=calendar.month(2008,3)

>>> print cal
'''SyntaxError: Missing parentheses in call to 'print'. Did you mean print(cal)?'''

>>> print (cal)

     March 2008

Mo Tu We Th Fr Sa Su

                1  2

 3  4  5  6  7  8  9

10 11 12 13 14 15 16

17 18 19 20 21 22 23

24 25 26 27 28 29 30

31



#functions

>>> def printme(str):
	'this will be printed'
	print(str)
	return;


>>> printme('blabla')

blabla



>>> def changeme(mylist):
	mylist.append([23]);
	print(mylist)
	return


>>> a=[12]

>>> a
[12]

>>> changeme(a)
[12, [23]]

>>> changeme(a);
[12, [23], [23]]

>>> trytryagain = lambda x, y : x + y
>>> trytryagain(1,1)
2

>>> def functest(list):
	list.pop()
	print(list)
	
>>> newlist=[1,2,3,45,6,77,23]
>>> functest(newlist)
[1, 2, 3, 45, 6, 77]

>>> try
SyntaxError: invalid syntax
>>> try:
	if name>3: #will give error
		print ("hellooo")
except:
	print("i told you so")

	
i told you so



>>> def noyearsleft(name,age):
        a=100-age
        print('your name is: ' +name +' and you are: '+age+' years old')
        print('you have %d years left till 100'%(a))
    

>>> noyearsleft('cristina',29)
'''
TypeError                                 Traceback (most recent call last)
<ipython-input-28-8feb4f95a1e3> in <module>()
----> 1 noyearsleft('cristina',29)

<ipython-input-27-2d825e14bbd3> in noyearsleft(name, age)
      1 def noyearsleft(name,age):
      2     a=100-age
----> 3     print('your name is: ' +name +' and you are: '+age+' years old')
      4     print('you have %d years left till 100'%(a))
      5 

TypeError: Can't convert 'int' object to str implicitly
'''

>>> def noyearsleft(name,age):
      a=100-age  
      print('your name is: ' +name +' and you are: '+str(age)+' years old')
      print('you have %d years left till 100'%(a))
  

>>> noyearsleft('cristina',29)
your name is: cristina and you are: 29 years old
you have 71 years left till 100




>>> def noyearsleft():
        name=input('please state your name: ')
        age=input('please state you age: ')
        print('your name is %s and you are %d years old'%(name,int(age)))
        a=100-int(age)
        print('you have %d years left till 100'%(a))
    

>>> noyearsleft()

please state your name: cristina

please state you age: 29
your name is cristina and you are 29 years old
you have 71 years left till 100




>>> number=input('please enter a number: ')

please enter a number: 11

>>> int(number)
11

>>> if 11%2==0:
        print('this is an even no')
    else:    
        print('this is odd')
    
this is odd



>>> a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

>>> for i in range(len(a)):
        if a[i]<5:
           print(a[i])
        i=i+1    
    
1
1
2
3




#modules

>>>import fibo
'''
ImportError                               Traceback (most recent call last)
<ipython-input-1-4105c89a6fa8> in <module>()
----> 1 import fibo

ImportError: No module named 'fibo'
'''

>>>import os

>>>cwd=os.getcwd()

cwd
'C:\\Program Files\\Continuum\\Anaconda3'

>>>os.chdir('C:\Users\neaccri\Desktop')
'''  File "<ipython-input-5-7611d4aef532>", line 1
    os.chdir('C:\Users\neaccri\Desktop')
            ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
'''

>>>os.getcwd()
'C:\\Program Files\\Continuum\\Anaconda3'

>>>os.chdir('C:\\Users\\neaccri\\Desktop')

>>>os.getcwd()
'C:\\Users\\neaccri\\Desktop'

>>>import fibo
'''ImportError                               Traceback (most recent call last)
<ipython-input-9-4105c89a6fa8> in <module>()
----> 1 import fibo

ImportError: No module named 'fibo'
'''

>>>os.chdir('H:\\config\\Desktop')

>>>os.getcwd()
'H:\\config\\Desktop'

>>>import fibo
>>>fibo.fib(1000)
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 

>>>fibo.fib2(100)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

>>>fibo.__name__
'fibo'



```
