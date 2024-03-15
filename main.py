# from Paquet_de_carte import Carte
from Manipulation_carte import *
# from gerer_erreur import *
from mecanique_jeux import *

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("                 BLACKJACK                 ")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")


def calucler_total(carte_1, carte_2):
    carte_1 = convertir_une_carte(carte_1)
    carte_2 = convertir_une_carte(carte_2)
    total_premier = int(carte_1[0]) + int(carte_2[0])
    return total_premier


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
            f"Voila vos deux cartes: le {carte1[0]} de {carte1[1]} et le {carte2[0]} de {carte2[1]}"
            f" pour un total de {total}")
        choix = choix_piocher_ou_non()
        if choix == "piocher":
            total, carte3 = piocher(total)
            if total > 21:
                parti_en_cours = buster(total)
            elif total < 21:
                print(f"Vous avez piocher le {carte3[0]} de {carte3[1]} pour un nouveau total de {total}")
                if total > 21:
                    buster(total)
                    parti_en_cours = buster(total)
        elif choix.lower() == "rester":
            rester()  # fonction a complété
            pass
        if not parti_en_cours:
            break

else:
    print("Merci et à la prochaine")
