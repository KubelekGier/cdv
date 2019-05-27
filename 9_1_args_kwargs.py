#### 
def wys(num1,num2):
	print(f'num1:{num1}')
	print(f'num2:{num2}\n\n')
wys(2,4)



############### *args
def wys_args(num1,*args):
	print(f'num1:{num1}')
	for i in args:
		print(f'nastepny element:{i}')
wys_args(2,4,32,44)

######## *kwargs

import os
os.system('cls')

def prac(**kwargs):
	print(kwargs)
	for key,value, in kwargs.items():
		print(f'klucz {key}, wartosz {value}')
	
pracownik1 = {
	'imie':"janusz",
	'naz':"nowak",
	'wiek':21,
	'city' : "poznan",
	'prac' : True
}
prac(**pracownik1)