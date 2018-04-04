import re,os

def countword(filename):
	try:
		file=open(filename,'r')
		list_words=[]
		lines=file.readlines()
		for l in lines:
			list_words.extend(l.split(" "))
		mylist=[re.sub(r'[^A-Za-z0-9]+', '', x) for x in list_words]#[^A-Za-z0-9]+ matches a string of characters that  are not leters or numbers
		#'\W' same as [^A-Za-z0-9]+	
		counter=0
		for i in range(len(mylist)):
			if mylist[i]=='felis':
				counter=counter+1
			i=i+1    
		print('The word occurs: ',counter,' times')
		file.close()
	except FileNotFoundError:
		print("The file doesn't exist in your current working path \nPlease add 'input.txt' file to: ", os.getcwd())
	except IOError:
		print("An error occured trying to read the file")
		
if __name__ == '__main__':
	countword('input.txt')