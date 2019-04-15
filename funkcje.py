def witaj():
    print('witaj')

witaj()

def wyswietlwiek(wiek):
    print(f'twoj wiek{wiek}')

wyswietlwiek(23)

def iloczyn(a,b):
    return a*b

print(iloczyn(3,4))

def iloraz(a,b):
    return a/b
x=iloraz(4,5)
print(f'iloraz to {x}')
print(type(x))

print(iloraz(b=10, a=3))

'''
User podaje marke, model, pojemnosc, predkosc max,

utworz funkcje ktora bierze dane od user i przepisze so slowinika
utorz druga funkcje wyswietlajaca w danycm formacie
marka
model
...
'''

def adb(z,x,c,v):
    z=input('podaj marke')
    x=input('podaj model')
    c=input('podaj pojemnosc')
    v=input('podaj predkosc max')

def ytu(z,x,c,v):
    print(f'marka to {z}')
    print(f'marka to {x}')
    print(f'marka to {c}')
    print(f'marka to {v}')

adb(z,x,c,v)
ytu(z,x,c,v)
