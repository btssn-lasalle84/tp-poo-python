#!/usr/bin/python3
# coding: utf-8

a = 1 # un entier
b = 2.5 # un float
c = "hello" # une chaine de caracteres

# afficher le type d'une variable :
print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'str'>

# transtypage :
a = int(b) # a vaut 2

# vérifier le type d'une variable :
print(isinstance(a, int))