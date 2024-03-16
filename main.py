# from Paquet_de_carte import Carte
from Manipulation_carte import *
# from gerer_erreur import *
from mecanique_jeux import *

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("                 BLACKJACK                 ")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

jouer = input("Bonjour, voulez-vous jouez au BlackJack ? Oui/Non: ")

jouer = recomencer_partit(jouer)

if jouer.lower() == "oui":
    parti_en_cours = True
    while parti_en_cours:
        print("/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*")
        print("Le groupier vas vous donnez 2 cartes, vous devez choisir si vous voulez une autre carte ou vous garder "
              "ces cartes.")
        carte1 = obtenir_une_cartes()
        carte2 = obtenir_une_cartes()
        carte3 = obtenir_une_cartes()
        total = calculer_total(carte1, carte2)
        print(
            f"Voila vos deux cartes: le {carte1[0]} de {carte1[1]} et le {carte2[0]} de {carte2[1]}"
            f" pour un total de {total}")
        print(f"La carte du Croupier est le {carte3[0]} de {carte3[1]}")
        choix = choix_piocher_ou_non()
        total = plus_petit_que21(total, choix, carte3)
        if total > 21:
            parti_en_cours = buster(total)
        elif total < 21:
            choix = choix_piocher_ou_non()
            total = plus_petit_que21(total, choix, carte3)
            if total > 21:
                parti_en_cours = buster(total)
            if total < 21:
                choix = choix_piocher_ou_non()
                total = plus_petit_que21(total, choix, carte3)
                if total > 21:
                    parti_en_cours = buster(total)
                if total < 21:
                    plus_petit_que21(total, "rester", carte3)
        elif total == 21:
            print("total est de 21")

        elif not parti_en_cours:
            break


else:
    print("Merci et à la prochaine")
