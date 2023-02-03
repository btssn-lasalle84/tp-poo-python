#!/usr/bin/python3
# coding: utf-8

# la première ligne (ci-dessus) commence par #! (le shebang) qui permet d'indiquer
# le chemin vers l'interpréteur avec lequel le script doit être exécuté

# Python utilise le retour chariot pour séparer les instructions, deux points (:) et l’indentation pour séparer les blocs de code.
# Les blocs de code (fonctions, instructions if, boucles for ou while etc.) sont définis par leur indentation. 
# L'indentation démarre le bloc et la désindendation le termine. 
# Il n’y a pas d’accolades, de crochets ou de mots clés spécifiques.

# Typage : dynamique, fort

class Vehicule:
    """La classe Vehicule"""
    _modele = ""
    couleur = ""

    def __init__(self, modele="", couleur=""):
        self._modele = modele
        self.couleur = couleur
    
    def affiche(self): 
        print("modele = " + self._modele)
        print("couleur = " + self.couleur)

v1 = Vehicule()

print("Vehicule v1")
v1.affiche()

v1.couleur = "rouge"
#v1.couleur = 1 # typage fort !
print("La couleur du vehicule v1 est " + v1.couleur)
v1.modele = "renault"

print("Vehicule v1")
v1.affiche()

v2 = Vehicule("peugeot", "blanche")

print("Vehicule v2")
v2.affiche()
