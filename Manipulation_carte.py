from Paquet_de_carte import Carte

def obtenir_une_cartes():
    carte = Carte()
    carte = carte.tirer_une_carte()

    return carte

def convertir_une_carte(carte):
    cartes = list(carte)
    if cartes[0] == "Valet":
        cartes[0] = "10"
    elif cartes[0] == "Dame":
        cartes[0] = "10"
    elif cartes[0] == "Roi":
        cartes[0] = "10"
    elif cartes[0] == "As":
        cartes[0] = "1"

    return tuple(cartes)

def donner_nouvelle_carte(function):
    carte = obtenir_une_cartes()
    carte = convertir_une_carte(carte)

    return carte