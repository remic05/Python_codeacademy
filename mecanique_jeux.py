from Manipulation_carte import donner_nouvelle_carte, convertir_une_carte
from gerer_erreur import choix_piocher_ou_rester, recomencer_partit

parti_en_cours_ = True


def calculer_total(carte_1, carte_2):
    carte_1 = convertir_une_carte(carte_1)
    carte_2 = convertir_une_carte(carte_2)
    total_premier = int(carte_1[0]) + int(carte_2[0])
    return total_premier


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
    carte = donner_nouvelle_carte()
    total_second += int(carte[0])
    return total_second, carte


def rester(total, carte1):
    total_croupier2 = 0
    print(f"Très bien votre total est alors de {total}, regardon maintenant ce que le croupier a obtenu ")
    carte2 = donner_nouvelle_carte()
    total_croupier1 = croupier_total(carte1, carte2)
    print(f"Le croupier à piocher sa deuxième carte et à obtenu le {carte2[0]} de {carte2[1]} pour un total "
          f"maintenant à {total_croupier1}")
    while total_croupier1 < 17 and total_croupier2 < 17:
        total_2, carte = piocher(total_croupier1)
        total_2 += total_croupier2
        total_croupier2 = total_2
        print(
            f"Le croupier à maintenant piocher le {carte[0]} de {carte[1]} pour un nouveau total de {total_croupier2}")

    return total_croupier2


def croupier_total(carte1, carte2):
    total = calculer_total(carte1, carte2)

    return total


def choix_piocher_ou_non():
    choix = input("Voulez vous une autre carte ou vous souhaiter garder cela ? rester/piocher ")
    choix = choix_piocher_ou_rester(choix)

    return choix


def plus_petit_que21(total, choix, carte3):
    if choix == "piocher":
        total, carte = piocher(total)
        if total < 21:
            print(f"Vous avez piocher le {carte[0]} de {carte[1]} pour un nouveau total de {total}")
        return total
    elif choix.lower() == "rester":
        total_croupier = rester(total, carte3)
        print(gagnant(total, total_croupier))
        continuer_apres_buster = input("Voulez vous recommencer ? Oui ou non ? ")
        recomencer_partit(continuer_apres_buster)

        return continuer_apres_buster


def gagnant(total1, total2):
    if total1 > total2:
        return f"Bravo vous avez gagné avec un total de {total1} le groupier avais seulement {total2}"
    elif total2 > total1:
        return f"Le croupier a gagné avec un total de {total1} vous aviez seuelemnt {total2}"
