#!/usr/bin/python3
# coding: utf-8

# un commentaire : mon premier programme Python !

import sys

print(sys.version)
print()

# saisie d'une chaîne de caractères
langue = input("Quelle est votre langue ? (fr, ...)")

# une instruction conditionnelle
if langue == "fr" :
    message = "Bonjour le monde"
else :
    message = "Hello world"

# voir aussi : if ... elif ... else

# saisie d'un entier
nb = int(input("Donnez un nombre : "))
i = 0

# une boucle
while i < nb:
    #print(message)
    print(message, i + 1, " fois")
    i += 1
