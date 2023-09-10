import script3;

def test_script3(capfd):
    vehicule = script3.Vehicule("peugeot", "blanche")
    assert vehicule.couleur == "blanche"
    assert vehicule.modele == "peugeot"
