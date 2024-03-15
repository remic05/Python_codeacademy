class Carte:
    def __init__(self):
        self.paquet = self.creation_paquet()

    def creation_paquet(self):
        couleurs = ["Coeur", "Trèfle", "Pique", "Carreau"]
        valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        paquet = []

        for couleur in couleurs:
            for valeur in valeurs:
                paquet.append((valeur, couleur))
        return paquet

    def tirer_une_carte(self):
        import random
        carte_tiree = random.choice(self.paquet)
        self.paquet.remove(carte_tiree)
        return carte_tiree
