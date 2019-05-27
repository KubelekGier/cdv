### a2 +b dla c>0
## a-b2 dla c<0
## 1/a-b dla c =0
a=float(input('podaj liczbe a: '))
b=float(input('podaj liczbe b: '))
c=float(input('podaj liczbe c: '))
def dzialaj(a,b,c):
	if c>0:
		res = (a*a)+b
		print(f'{res}')
	if c<0:
		res = a-(b*b)
		print(f'{res}')
	if c==0:
		res = 1/(a-b)
		print(f'{res}')
dzialaj(a,b,c)