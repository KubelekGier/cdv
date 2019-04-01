tekst = "Anna, pawel, JuLIA"

lista = tekst.split(", ")
print (tekst)
print (lista)
print(type(lista)) #list
imie1 = lista[0]
print(imie1)

imieDuza = imie1.upper()
print(imieDuza)
imieMale = imie1.lower()
print(imieMale)
#spr zawartosci
nazwisko = ""
print(nazwisko.isalpha()) #false

print("\nPodaj swoje nazwisko ",end="")
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc) #true or false

text1 = "\nJulia\n"
text2 = "Nowak"
print(text1 + text2)

text1 = text1.rstrip()
print(text1 + text2)
print(text1 +" "+ text2)

#wyświetlenie łańcucha

#wszystkie wersje pythona

text = "%s, Java i %s" % ("php","python")
print(text)

#nowsze wersje
text="{1}, Java i {0}".format("PHP","Python")
print(text)

#help(text.replace)
new = text.replace("PHP", "C#")
print(new)

#wypisanie danych

rok = 2019
miesiac = 4
dzien = 1
print("\nData:", end="")
print(dzien,miesiac,rok)

print("\nData:", end="")
print(dzien,miesiac,rok, sep="-")

























print()
