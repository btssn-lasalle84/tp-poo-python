<img alt="points bar" align="right" height="36" src="../../blob/badges/.github/badges/points-bar.svg" />

![](https://img.shields.io/badge/Github-Classroom-green.svg) ![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=plastic)

# TP POO : Python

- [TP POO : Python](#tp-poo--python)
  - [Le langage Python](#le-langage-python)
    - [Présentation](#présentation)
    - [Le typage](#le-typage)
  - [La syntaxe](#la-syntaxe)
  - [Interprétation de code POO](#interprétation-de-code-poo)
  - [Travaux pratiques](#travaux-pratiques)
    - [Pré-requis](#pré-requis)
    - [Travail demandé](#travail-demandé)
  - [Tests unitaires](#tests-unitaires)
  - [Bac à sable et développement en ligne](#bac-à-sable-et-développement-en-ligne)

**Les objectifs de ce TP sont de s’initier à la programmation Python en transférant ses connaissances de la programmation orientée objet.**

> Pour les enseignants, ceci est un "petit" devoir pour [Github Classroom](https://btssn-lasalle84.github.io/guides-developpement-logiciel/guide-classroom.html). Il montre l'utilisation des [tests unitaires](#tests-unitaires) en Python, la notation automatique et l'insertion d'un badge pour l'affichage de la note.

## Le langage Python

Cette partie présente les éléments essentiels à connaître sur Python. Evidemment, cela ne remplace pas un cours ou la documentation officielle du langage.

### Présentation

Python est un langage de programmation interprété. Il permet la programmation orientée objet. Il est doté d’un typage dynamique fort, d’une gestion automatique de la mémoire par ramasse-miettes et d’un système de gestion d’exceptions.

> En 1989, profitant d’une semaine de vacances durant les fêtes de Noël, le programmeur Guido van Rossum utilise son ordinateur personnel pour écrire la première version du langage. Fan de la série télévisée Monty Python’s Flying Circus, il décide de baptiser ce projet Python. La première version publique (numéroté 0.9.0) date de février 1991. Guido van Rossum est le principal auteur de Python, et son rôle de décideur central permanent est reconnu avec humour par le titre de « Dictateur bienveillant à vie ».

Le langage Python est placé sous une licence libre et fonctionne sur la plupart des plates-formes informatiques (Windows, Unix, GNU/Linux, macOS, Android, iOS, ...).

> CPython est l’implémentation de référence du langage Python. C’est un interpréteur de _bytecode_ écrit en langage C. C’est un logiciel libre.

Python est un langage qui peut s’utiliser dans de nombreux contextes et s’adapter à tout type d’utilisation grâce à des bibliothèques spécialisées. Il est cependant particulièrement utilisé comme langage de script pour automatiser des tâches simples mais fastidieuses. Il est particulièrement répandu dans le monde scientifique, et possède de nombreuses bibliothèques optimisées destinées au calcul numérique (notamment dans la _data science_). Python est aussi utilisé comme langage de programmation dans l’enseignement élémentaire et supérieur, notamment en France.

> Le Zen de Python est un ensemble de 19 principes qui influencent le design du langage de programmation Python, et sont utiles pour comprendre et utiliser le langage : https://fr.wikipedia.org/wiki/Zen_de_Python

Ressources :

- Site officiel : https://www.python.org
- Documentation Python 3 : https://docs.python.org/fr/3/
- Documentation Python 2 : https://docs.python.org/fr/2/
- Le tutoriel Python 3 : https://docs.python.org/fr/3/tutorial/
- Le tutoriel Python 2 : https://docs.python.org/fr/2/tutorial/
- Une présentation : http://tvaira.free.fr/dev/python/cours-python.html

> Deux versions du langage Python ont longtemps cohabité : la version 2 (appelé _python legacy_) et la version 3. L’annonce de la fin de Python 2 pour le 31 décembre 2019 va définitivement accélérer le processus de migration vers la version 3.

Le langage Python est un des langages les plus populaires actuellement :

![](images/tiobe.png)

> Langages proches : Perl, Ruby, Scheme, Smalltalk et Tcl.

### Le typage

Tous les langages de programmation permettent de manipuler des valeurs avec des variables.

Le typage d’une variable consiste à associer à son nom un « type » de donnée.

> Pour rappel, le « type » est la convention d’interprétation (codage) de la séquence de bits qui constitue la variable. Le type de la variable spécifie aussi la longueur de cette séquence (8 bits, 32 bits, 64 bits, ...).

Suivant les langages de programmation, il existe plusieurs manières de considérer le typage :

- Typage statique : il consiste à demander au programmeur de déclarer expressément chaque variable en indiquant son type. Exemples de langage à typage statique : C, C++, Java, C#
- Typage dynamique : il consiste à laisser l’interpréteur réaliser cette opération de typage « à la volée » lors de l’exécution du code. C’est la valeur affectée à la variable qui précisera son type.
Exemples de langage à typage dynamique : PHP, Perl, **Python**, Javascript, bash (shell Linux)
- Typage fort : Un langage de programmation est dit fortement typé lorsqu’il garantit que les types de données employés décrivent correctement les données manipulées. Exemples de langage fortement typé : C++, Java, C#, **Python**
- Typage faible : Un langage de programmation est dit faiblement typé lorsqu’il ne considère pas comme une erreur les changements de types. Exemples de langage faiblement typé : PHP, Javascript, C (car il accepte les transtypages implicites comme par exemple `int` vers `short`)

Le langage Python est doté d’un **typage dynamique fort**.

Exemple d’utilisation des types en Python (`type.py`) :

```python
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
```

## La syntaxe

Python utilise pour séparer les instructions : le retour chariot, les deux points (`:`)

Les blocs de code (fonctions, instructions `if`, boucles `for` ou `while` etc.) sont définis par leur indentation après les deux points (`:`).

L’indentation démarre le bloc et la désindendation le termine.

> Il n’y a donc pas d’accolades, de crochets ou de mots clés spécifiques.

## Interprétation de code POO

Soit le script Python `poo.py` :

```python
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
```

Question 1. Qu’est-ce que `Vehicule` ?

Question 2. Qu’est-ce que `v1` ?

Question 3. Qu’est-ce que `couleur` ?

Question 4. Qu’est-ce que `affiche()` ?

Question 5. Qu’est-ce que fait `affiche()` ?

Question 6. Qu’est-ce que `__init__` ?

> A compléter dans le fichier `compte-rendu.md` (au format [Markdown](https://guides.github.com/features/mastering-markdown/)) fourni.

## Travaux pratiques

### Pré-requis

Programmer en Python sous Ubuntu : https://doc.ubuntu-fr.org/python

Version de Python :

```sh
$ python3 --version
Python 3.6.8
```

Il est possible de programmer directement dans l’interpréteur Python en mode CLI :

```sh
$ python
Python 2.7.15+ (default, Oct 72019, 17:39:04)
[GCC 7.4.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 1
>>> print a
1
>>> exit()
```

Le script Python `helloworld3.py` :

```python
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

```

> La première ligne sert à préciser le chemin de l’interpréteur précédé des caractères `#!` (le _shebang_) qui exécutera le script. Cette ligne est inutile dans le cas d’une programmation web.

Il existe plusieurs manières d’exécuter un script Python de façon locale (mode CLI) :

- le rendre exécutable :

```sh
$ chmod +x helloworld3.py
$ ./helloworld3.py
```

- utiliser l’interpréteur Python :

```sh
$ python3 helloworld3.py
```

### Travail demandé

Pour l’écriture d’un programme orientée objet en Python, on désire disposer du concept d’`Article`.

Notre article doit posséder une designation et un prix. Il est possible d’obtenir la designation et le prix d’un article. Lorsque l’on crée un article, il est possible de préciser sa designation et son prix sinon il aura des valeurs nulles par défaut.

![](images/classe-article.png)

Fournir un programme `article.py` qui permet de répondre aux questions suivantes :

Question 7. Implémenter la classe `Article`.

Question 8. Instancier un objet `article1` en utilisant le constructeur par défaut et un objet `article2` dont la désignation est "Le Trône de fer, Tome 1" avec un prix de 13.29 euros.

Question 9. Donner l’instruction qui permet d’afficher simplement le prix de l'`article2`.

Question 10. Ajouter une méthode `affiche()` qui affichera la designation et le prix de l’`Article` sous la forme "<designation> : <prix> euros", par exemple : "Le Trône de fer, Tome 1 : 13.29 euros". Afficher l'`article2` avec la méthode `affiche()`.

_Bonus :_ Afficher l’aide (_docstring_) sur la méthode `affiche()`.

## Tests unitaires

Installation de `pytest` :

```sh
$ sudo apt -y install python3-pip
$ sudo -H pip3 install pytest
```

Lancement des tests pour le TP :

```sh
$ pytest article1_test.py
$ pytest article2_test.py
$ pytest article3_test.py
```

Exemples :

- tester un script `script1.py` (avec _stdin/stdout_)

```python
# Ce script demande à l’utilisateur de saisir un nombre et le stocke dans la variable a puis affiche le résultat de a*3.

a = int(input())
# print(type(a)) # <class 'int'>
print(a*3)
```

Le programme de test `test_script1.py` :

```python
import pytest;
import runpy;
from io import StringIO

def test_script1(monkeypatch,capfd):
    # simule une saisie
    monkeypatch.setattr('sys.stdin', StringIO('3\n'))
    # voir aussi : simule input()
    #monkeypatch.setattr('builtins.input', lambda _: "3")
    # exécute le script à tester
    runpy.run_path("script1.py")
    # vérifie la sortie produite
    out, err = capfd.readouterr()
    assert out == "9\n"
```

Test :

```sh
$ pytest test_script1.py
================================================================================================== test session starts ===================================================================================================
platform linux -- Python 3.10.12, pytest-7.2.1, pluggy-1.0.0
rootdir: /mnt/sda/home/tv/Documents/git/tp-poo-python
collected 1 item

test_script1.py .                                                                                                                                                                                                  [100%]

=================================================================================================== 1 passed in 0.01s ====================================================================================================
```

- tester une fonction dans `script2.py` :

```python
# Ce script définit une fonction qui reçoit en argument une température en degrés Celsius et la retourne en degrés Fahrenheit.

def convertirCelsiusVersFahrenheit(C):
    """reçoit en argument une température en degrés Celsius et la retourne en degrés Fahrenheit.
    """
    return C * 9/5 + 32
```

Le programme de test `test_script2.py` :

```python
import script2;
import pytest;

def test_script2():
    F = script2.convertirCelsiusVersFahrenheit(22)
    assert F == pytest.approx(71.6, 0.1)
    F = script2.convertirCelsiusVersFahrenheit(0)
    assert F == 32
    F = script2.convertirCelsiusVersFahrenheit(-100)
    assert F == -148
```

Test :

```sh
$ pytest test_script2.py
================================================================================================== test session starts ===================================================================================================
platform linux -- Python 3.10.12, pytest-7.2.1, pluggy-1.0.0
rootdir: /mnt/sda/home/tv/Documents/git/tp-poo-python
collected 1 item

test_script2.py .                                                                                                                                                                                                  [100%]

=================================================================================================== 1 passed in 0.00s ====================================================================================================
```

- tester une classe dans `script3.py` :

```python
class Vehicule:
    """La classe Vehicule"""

    def __init__(self, modele="", couleur=""):
        self.modele = modele
        self.couleur = couleur

    def affiche(self):
        print("modele = " + self.modele)
        print("couleur = " + self.couleur)
```

Le programme de test `test_script3.py` :

```python
import script3;

def test_script3(capfd):
    vehicule = script3.Vehicule("peugeot", "blanche")
    assert vehicule.couleur == "blanche"
    assert vehicule.modele == "peugeot"
```

Test :

```sh
$ pytest test_script3.py
================================================================================================== test session starts ===================================================================================================
platform linux -- Python 3.10.12, pytest-7.2.1, pluggy-1.0.0
rootdir: /mnt/sda/home/tv/Documents/git/tp-poo-python
collected 1 item

test_script3.py .                                                                                                                                                                                                  [100%]

=================================================================================================== 1 passed in 0.00s ====================================================================================================
```

Voir aussi pour [Jupyter](https://jupyter.org/) :

- [nbgrader](https://nbgrader.readthedocs.io/en/stable/index.html)
- [Teaching Courses with GitHub and Jupyter Notebooks](https://sites.duke.edu/ilearninglab/files/2020/12/Teaching-Courses-with-GitHub-and-Jupyter-Notebooks.pdf)

## Bac à sable et développement en ligne

Il est souvent nécessaire de passer par un "bac à sable".

> En informatique, le bac à sable (_sandbox_) est une zone d'essai permettant d'exécuter des programmes en phase de test ou dans lesquels la confiance est incertaine. C'est notamment très utilisé en sécurité informatique pour sa notion d'isolation.

Il existe de nombreux sites web qui fournissent des EDI (Environnement de Développement Intégré) en ligne pour tester du code ou des services : un espace d'apprentissage séparé. Ils permettent aussi d'échanger des exemples.

Quelques sites :

- Coding Ground For Developers : https://www.tutorialspoint.com/codingground.htm pour tout !
    - **Python : https://www.tutorialspoint.com/execute_python3_online.php**
    - Markdown : https://www.tutorialspoint.com/online_markdown_editor.php
- Visual Studio Code Online : https://vscode.dev/
- Gitpod : https://www.gitpod.io/
- Codeanywhere (Cloud IDE) : https://codeanywhere.com/

Exercices d’entraînement : http://tvaira.free.fr/dev/python/exercices-python.html

---
Thierry Vaira : **[thierry(dot)vaira(at)gmail(dot)com](thierry.vaira@gmail.com)**
