from Manipulation_carte import obtenir_une_cartes, donner_nouvelle_carte
from gerer_erreur import choix_piocher_ou_rester, recomencer_partit
from main import total


def buster_message(total):
    print("Vous avez \"Buster\" perdu pour ce tour avec un total de {}".format(total))
    continuer_apres_buster = input("Voulez vous recommencer ? Oui ou non ? ")
    recomencer_partit(continuer_apres_buster)

    return continuer_apres_buster


def buster():
    global parti_en_cours
    continuer_apres_buster = buster_message(total)
    if continuer_apres_buster.lower() == "oui":
        parti_en_cours = True

    elif continuer_apres_buster.lower() == "non":
        parti_en_cours = False
        print("Merci et à la prochaine")

    return parti_en_cours


def piocher(total_second):
    carte3 = donner_nouvelle_carte(obtenir_une_cartes())
    total_second += int(carte3[0])
    return total_second, carte3


def rester():
    pass


def choix_piocher_ou_non():
    choix = input("Voulez vous une autre carte ou vous souhaiter garder cela ? rester/piocher ")
    choix = choix_piocher_ou_rester(choix)

    return choix