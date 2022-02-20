'''
1. Feladat
Írj egy programot, amely 5 darab véletlenszámot generál [1;7] intervallumon, és ezeket eltárolja egy listában. Kérjen be a felhasználótól egy számot, és vizsgálja meg, hogy ez előfordul-e a listában! Az eredményről tájékoztassa a felhasználót, és írja ki a lista elemeit a képernyőre!
'''

from random import randint

lista = []

for szamok in range(5):
    szamok = randint(1,7)
    lista.append(szamok)
    
beker = int(input('Szám: '))

if beker in lista:
    print('Benne van a listában.')
else:
    print('Nincs benne a listában.')

print(lista)