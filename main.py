from Paquet_de_carte import Carte
from Manipulation_carte import *
from gerer_erreur import *
from mecanique_jeux import  *
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("                 BLACKJACK                 ")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

def calucler_total(carte1, carte2):
    carte1 = convertir_une_carte(carte1)
    carte2 = convertir_une_carte(carte2)
    total = int(carte1[0]) + int(carte2[0])
    return total


jouer = input("Bonjour, voulez-vous jouez au BlackJack ? Oui/Non: ")

jouer = recomencer_partit(jouer)

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
            total, carte3 = piocher(total)
            if total > 21:
                buster()
            elif total < 21:
                print(f"Vous avez piocher le {carte3[0]} de {carte3[1]} pour un nouveau total de {total}")
                if total > 21:
                    buster()
        elif choix.lower() == "rester":
            rester()  # fonction a complété
            pass
        if not parti_en_cours:
            break

else:
    print("Merci et à la prochaine")
