class Vehicule:
    """La classe Vehicule"""

    def __init__(self, modele="", couleur=""):
        self.modele = modele
        self.couleur = couleur

    def affiche(self):
        print("modele = " + self.modele)
        print("couleur = " + self.couleur)
