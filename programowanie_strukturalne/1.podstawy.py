print("CDV")
print(10)
#komentarz
'''
kom w wielu
liniach
'''
#potegowanie
potega = 2 ** 10
print(potega)
#pobieranie danych z klawiatury
imie= input()

#konkatenacja +
print ("Twoje imie podane z klawiatury: "+imie)
nazwisko = input("Podaj nazwisko: ")
print("Nazwisko to", nazwisko)

#Twoje imie i nazwisko
print("Twoje imie: ",imie,". Twoje nazwisko: ",nazwisko)

'''
Użytkownik podaj swój wiek z kla
wyświetl dane w formacie: Twój wiek [wiek] lat
'''
print("Podaj swoj wiek ",end="")
wiek=input()
print(type(wiek)) #str
print("Twoj wiek ", wiek, "lat")
print("Twoj wiek "+ wiek+ " lat")

wiek1 = 20
print(type(wiek1))
wiek1=str(wiek1)
print("Twoj wiek ", wiek1, "lat")
print("Twoj wiek "+ wiek1+ " lat")

nazwisko="Kowalski"
pierwszyZnak = nazwisko[0]
print(pierwszyZnak)
'''
dlugosc = len(nazwisko)
print("Dlugosc: "+dlugosc)
'''
ostatniZnak = nazwisko[len(nazwisko)-1]
print("Dlyugosc znaku",ostatniZnak)

ostatniZnak = nazwisko[-1]
print("Dlyugosc znaku",ostatniZnak)

#konwersja
x = 5
print(type(x)) #str
x = int(x)
print(type(x)) #int


y = 10
print(type(y)) #int
y=y/2
print(type(y)) #int
print(y)

nazwisko = "Kowalski"
print(nazwisko[0]) #K
print(nazwisko[0:3]) #Kow
print(nazwisko[-2]) #k
print(nazwisko[-2:]) #ki
print(nazwisko[:-2]) #Kowals
print(nazwisko[:-2:2]) #Kwl














print()
