#przekazywanie arg przez referencje
def show(name):
	print (f'przed modyfikacja '{name})
	name[0]="beata"
	name[1]="barbara"
	name[2]="bogdan"
	print(f'po mod':{name})
	print(f'id po mod'{id(name)})
	