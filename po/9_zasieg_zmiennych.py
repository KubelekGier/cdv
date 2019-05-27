#zmienne globalne i lokalneabs
x= "{0: 3f}".format(5)
print(x) #5.000

#napisz fukcje, ktora jako arg przyjmuje wart zlotych i zamienia dane o kursie dzisiejszym franka, wyswietl uzytkownikowi ile frankow kupi za podana kwote
def waluta(value):
	frank=3.8168
	wynik=value // frank
	print(f'ilosc frankow{wynik}')
waluta(500)
#zmienna globalna
zmienna_glob=10
print(f'wart {zmienna_glob}')
print(f'id {id(zmienna_glob)}')


def spr():
	global zmienna_glob
	zmienna_glob=20
	print(f'wart wew fun {zmienna_glob}')
	print(f'wart wew fun {id(zmienna_glob)}')
spr()
print(f'wart wew fun {zmienna_glob}')
print(f'wart wew fun {id(zmienna_glob)}')
