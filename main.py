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
        cartes[0] = "10"
    elif cartes[0] == "Dame":
        cartes[0] = "10"
    elif cartes[0] == "Roi":
        cartes[0] = "10"
    elif cartes[0] == "As":
        cartes[0] = "1"

    return tuple(cartes)


def calucler_total(carte1, carte2):
    carte1 = convertir_une_carte(carte1)
    carte2 = convertir_une_carte(carte2)
    total = int(carte1[0]) + int(carte2[0])
    return total


def donner_nouvelle_carte(function):
    carte = obtenir_une_cartes()
    carte = convertir_une_carte(carte)

    return carte


def erreur(jouer_encore):
    while jouer_encore.lower() != "oui" and jouer_encore.lower() != "non":
        jouer_encore = input("Veuillez entrer une valeur valide (Oui ou Non): ")

    return jouer_encore


def erreur2(choix):
    while choix.lower() != "rester" and choix.lower() != "piocher":
        choix = input("Veuillez entrer une valeur valide (rester ou piocher): ")

    return choix


def buster(total):
    print("Vous avez \"Buster\" perdu pour ce tour avec un total de {}".format(total))
    continuer = input("Voulez vous recommencer ? Oui ou non ? ")
    continuer = erreur(continuer)

    return continuer


def piocher(total_second):
    carte3 = donner_nouvelle_carte(obtenir_une_cartes())
    total_second += int(carte3[0])
    return total_second


def rester():
    pass


def choix_piocher_ou_non():
    choix = input("Voulez vous une autre carte ou vous souhaiter garder cela ? rester/piocher ")
    choix = erreur2(choix)

    return choix


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
        choix = choix_piocher_ou_non()
        if choix == "piocher":
            total = piocher(total)
        if total > 21:
            continuer = buster(total)
            if continuer.lower() == "Oui":
                parti_en_cours = True
                break
            elif continuer.lower() == "Non":  # A VÉRIFIER
                parti_en_cours = False
                print("Merci et à la prochaine")
                break
        elif total < 21:
            print("Vous avez obtenu")
        elif choix.lower() == "rester":
            rester() #fonction a complété
            pass
        print("te")

else:
    print("Merci et à la prochaine")
