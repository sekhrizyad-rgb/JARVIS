
def detect_intent(commande):
    commande = commande.lower().strip()
    mots = commande.split()

    if not mots:
        return {"intent": "UNKNOWN"}

    premier_mot = mots[0]
    reste = " ".join(mots[1:]) if len(mots) > 1 else None

    if premier_mot in ["ouvre", "lance", "démarre"]:
        if reste:
            return {"intent": "OPEN_APP", "target": reste}
        return {"intent": "UNKNOWN"}

    if premier_mot in ["ferme", "arrête", "quitte"]:
        if reste:
            return {"intent": "CLOSE_APP", "target": reste}
        return {"intent": "EXIT_JARVIS"}

    if "heure" in commande:
        return {"intent": "GET_TIME"}

    if premier_mot in ["cherche", "recherche"]:
        if reste:
            return {"intent": "SEARCH_WEB", "query": reste}
        return {"intent": "UNKNOWN"}

    return {"intent": "UNKNOWN"}
