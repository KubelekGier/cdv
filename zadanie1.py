a=int(input('podaj liczbe a: '))
b=int(input('podaj liczbe b: '))
def licz(a,b):
	try:
		result = (((a*a)+b)/(((a*a)+(2*a*b)+(b*b))))
		print(f'{result}')
	except ZeroDivisionError:
		print(f'dzielisz przez 0')
licz(a,b)