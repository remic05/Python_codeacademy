def recomencer_partit(jouer_encore):
    while jouer_encore.lower() != "oui" and jouer_encore.lower() != "non":
        jouer_encore = input("Veuillez entrer une valeur valide (Oui ou Non): ")

    return jouer_encore


def choix_piocher_ou_rester(choix):
    while choix.lower() != "rester" and choix.lower() != "piocher":
        choix = input("Veuillez entrer une valeur valide (rester ou piocher): ")

    return choix
