#przekazywanie arg przez referencje
def show(name):
	print (f'przed modyfikacja {name}')
	name[0]="beata"
	name[1]="barbara"
	name[2]="bogdan"
	print(f'po mod:{name}')
	print(f'id po mod{id(name)}')
data=['Anna','Agnieszka','Andrzej']
print(f'przed wywolaniem funkcji show {data}')
print(f'id obiektu {id(show)}')
print()
show(data)
print(f'po wywolaniu show {data}')
################### słownik
print(f'\n\n slownik')
data1 ={0:'Artur', 1:'Andrzej'}
print(f'przed wywolaniem funkcji {id(data1)}')
show(data1)
########przekazywanie arg przez wartosc
print('\n\n')
def show1(city):
	print (f'przed modyfikacja {name}')
	name[0]="berlin"
	name[1]="londyn"
	print(f'po mod:{name}')
	print(f'id po mod{id(name)}')
miasto ={0:'poznan', 1:'gniezno'}
print(f'przed wywolaniem funkcji {miasto}')
print(f'przed wywolaniem funkcji {id(miasto)}')
show1(list(miasto))
print(f'po wywolaniu show1 {miasto}')
#######slownik 2
miasto1 = {
	0: "gniezno",
	1: "poznan"
}
print(f'przed wywolaniem funkcji {miasto1}')
print(f'przed wywolaniem funkcji {id(miasto1)}')
show1(dict(miasto1))
print(f'po wywolaniu show1 {miasto1}')

####### try except

def dziel(x,y):
	try:
		result = x/y
		print(f'{x} / {y} = {result}')
	except:
		print(f'dzielisz przez 0')
dziel(2,0) #ZeroDivisionError
dziel(2,5)