def detect_intent(commande):
    commande = commande.lower().strip()

    mots = commande.split()

    if not mots:
        return {"intent": "UNKNOWN"}

    premier_mot = mots[0]

    # --- OPEN_APP ---
    if premier_mot in ["ouvre", "lance", "démarre"]:
        if len(mots) > 1:
            target = mots[1]
            return {"intent": "OPEN_APP", "target": target}
        return {"intent": "UNKNOWN"}

    # --- CLOSE_APP ou EXIT_JARVIS ---
    if premier_mot in ["ferme", "arrête", "quitte"]:
        if len(mots) > 1:
            target = mots[1]
            return {"intent": "CLOSE_APP", "target": target}
        else:
            return {"intent": "EXIT_JARVIS"}

    # --- GET_TIME ---
    if "heure" in commande:
        return {"intent": "GET_TIME"}

    # --- SEARCH_WEB ---
    if premier_mot in ["cherche", "recherche"]:
        if len(mots) > 1:
            requete = " ".join(mots[1:])
            return {"intent": "SEARCH_WEB", "query": requete}
        return {"intent": "UNKNOWN"}

    # --- Rien reconnu ---
    return {"intent": "UNKNOWN"}
