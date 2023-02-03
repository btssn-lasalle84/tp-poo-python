#!/usr/bin/python
# coding: utf-8

# un commentaire : mon premier programme Python !

import sys

print(sys.version)
print()

# saisie d'une chaîne de caractères
print("Quelle est votre langue ? (fr, ...)")
langue = raw_input()

# une instruction conditionnelle
if langue == "fr" :
    message = "Bonjour le monde"
else :
    message = "Hello world"

# voir aussi : if ... elif ... else

# saisie d'un entier
print("Donnez un nombre : ")
nb = input()
i = 0

# une boucle
while i < nb:
    #print message
    print message, i + 1, " fois"
    i += 1
