#listy
programowanie = ['PHP', 'Python', 'Java']
print(type(programowanie))
programowanie.append('C#')
programowanie.append('PHP')
print(programowanie)
ile=programowanie.count('PHP')
print(f'ile razy jest php {ile}')

#tuple
imiona = ('Julia','Anna', 'Tomek')
print(imiona)
print(type(imiona))
pierwszy = imiona[0]
print(pierwszy)
#slownik
osoba = {
    'imie':'Julia',
    'nazwisko':'Kowalski',
    'wiek':23
}
print(osoba)
print(type(osoba))
print (osoba['imie'])
print(osoba.keys())
print(osoba.get('wzrost','brak danych'))


#######################
#utworz slownik i przypiszz mu 3 imiona podane z klawiatury, wyswietl te dane na ekranie w formacie imie1:... itd
x=input('podaj imie1 ')
y=input('podaj imie2 ')
z=input('podaj imie3 ')




person = {
    'imie1':x,
    'imie2':y,
    'imie3':z
}
print(f'imie1:{})
print(person[f'imie2'])
print(person[f'imie3'])
