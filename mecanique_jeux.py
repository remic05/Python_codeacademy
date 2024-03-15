from Manipulation_carte import donner_nouvelle_carte
from gerer_erreur import choix_piocher_ou_rester, recomencer_partit

parti_en_cours_ = True

def buster_message(total):
    print("Vous avez \"Buster\" perdu pour ce tour avec un total de {}".format(total))
    continuer_apres_buster = input("Voulez vous recommencer ? Oui ou non ? ")
    recomencer_partit(continuer_apres_buster)

    return continuer_apres_buster


def buster(total):
    global parti_en_cours_
    continuer_apres_buster = buster_message(total)
    if continuer_apres_buster.lower() == "oui":
        parti_en_cours_ = True

    elif continuer_apres_buster.lower() == "non":
        parti_en_cours_ = False
        print("Merci et à la prochaine")

    return parti_en_cours_


def piocher(total_second):
    carte3 = donner_nouvelle_carte()
    total_second += int(carte3[0])
    return total_second, carte3


def rester():
    pass


def choix_piocher_ou_non():
    choix = input("Voulez vous une autre carte ou vous souhaiter garder cela ? rester/piocher ")
    choix = choix_piocher_ou_rester(choix)

    return choix


def plus_petit_que21(total, choix):
    if choix == "piocher":
        total, carte = piocher(total)
        if total < 21:
            print(f"Vous avez piocher le {carte[0]} de {carte[1]} pour un nouveau total de {total}")
    return total
