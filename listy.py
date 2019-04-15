programowanie = ['Python','C#','JS','PHP','Java']

print(programowanie)
print(type (programowanie))

pierwszy = programowanie[0]
print('Pierwszy jezyk programowania ' + pierwszy)

trzyElementy = programowanie[0:3]
print(''+trzyElementy)

ostatni = programoanie [-1]
print('Pierwszy jezyk programowania ' + ostatni)


#dod ele do losujzlisty

programowania.append('R')
programowania.append('Python')
print (programowanie)


#zliczanie ele w liście

ile = programowanie.count('Python')
print(f'Python wystepuje{ile}razy')



#ilosc ele w liscie
 iloscele= len(programowanie)
 print(iloscele)


 #laczenie listy

print(f'\n\b(programowanie)')
inneJezyki = ['c', 'c++']
print('polaczenie list')
programowanie.extend(inneJezyki)
print(programowanie)


#czyszczenie

nowa = programowanie
print(f'Nowa list{nowa}')

programowanie.clear()
print(f'Nowa lista po wyczyszczeniu{nowa}')
print(f' lista programowanie po wyczyszczeniu{programowanie}')
