
```python
>>> import os

>>> os.getcwd()
'C:\\Program Files\\Continuum\\Anaconda3'

>>> os.chdir('H:\\config\\Desktop') #runned on windows

>>> os.getcwd()
'H:\\config\\Desktop'

#now I can execute my program since I've saved the script on desktop

>>> exec(open('finalasig.py').read())
The file doesn't exist in your current working path 
Please add 'input.txt' file to:  H:\config\Desktop

>>> #oops, that's embarassing. Let me save also the input on desktop 

>>> exec(open('finalasig.py').read())
The word occurs:  3  times

>>> #yay

# also if I change in the file the occurence I can see the updated result:


PS H:\config\Desktop> python .\finalasig.py
The word occurs:  3  times
PS H:\config\Desktop> python .\finalasig.py
The word occurs:  5  times
PS H:\config\Desktop> python .\finalasig.py
The word occurs:  0  times
PS H:\config\Desktop>

```
