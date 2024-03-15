from Paquet_de_carte import Carte

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("                 BLACKJACK                 ")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")


def obtenir_une_cartes():
    carte = Carte()
    carte = carte.tirer_une_carte()

    return carte


def convertir_une_carte(carte):
    cartes = list(carte)
    if cartes[0] == "Valet":
        cartes[0] = "11"
    elif cartes[0] == "Dame":
        cartes[0] = "12"
    elif cartes[0] == "Roi":
        cartes[0] = "13"
    elif cartes[0] == "As":
        cartes[0] = "1"

    return tuple(cartes)


def calucler_total(carte1, carte2):
    carte1 = convertir_une_carte(carte1)
    carte2 = convertir_une_carte(carte2)
    total = int(carte1[0]) + int(carte2[0])
    return total


def erreur(jouer_encore):
    while jouer_encore.lower() != "oui" and jouer_encore.lower() != "non":
        jouer_encore = input("Veuillez entrer une valeur valide (Oui ou Non): ")

    return jouer_encore


jouer = input("Bonjour, voulez-vous jouez au BlackJack ? Oui/Non: ")

jouer = erreur(jouer)

if jouer.lower() == "oui":
    parti_en_cours = True
    while parti_en_cours:
        print("Le groupier vas vous donnez 2 cartes, vous devez choisir si vous voulez une autre carte ou vous garder "
              "ces cartes.")
        carte1 = obtenir_une_cartes()
        carte2 = obtenir_une_cartes()
        total = calucler_total(carte1, carte2)
        print(
            f"Voila vos deux cartes: le {carte1[0]} de {carte1[1]} et le {carte2[0]} de {carte2[1]} pour un total de {total}")
        choix = input("Voulez vous une autre carte ou vous souhaiter garder cela ? Garder/Autre ")
        while choix.lower() != "garder" and choix.lower() != "autre":
            jouer = input("Veuillez entrer une valeur valide (Garder ou Autre): ")
        if choix.lower() == "garder":
            carte3 = obtenir_une_cartes()
            convertir_une_carte(carte3)
            total += int(carte3[0])
            if total > 21:
                print("Vous avez \"Buster\" perdu pour ce tour")
                parti_en_cours = input("Voulez vous recommencer ? Oui ou non ? ")
            print("Vous avez obtenu")
        break

else:
    print("Merci et à la prochaine")
