def nwd(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a

a=int(input('podaj pierwsza liczbe '))
b=int(input('podaj druga liczbe '))
print(f'nwd: {nwd(a,b)}')
