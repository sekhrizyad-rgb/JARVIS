import os
from apps_registry import resolve_app


def close_app(target):
    nom, app = resolve_app(target)
    if app is None:
        return f"Je ne connais pas l'application '{target}'."
    process = app["process_name"]
    try:
        result = os.system(f"taskkill /im {process}")
        if result == 0:
            return f"Demande de fermeture envoyée à {nom}."
        return f"{nom} n'a pas pu être fermé normalement (non ouvert, ou ne répond pas à une fermeture standard)."
    except Exception as e:
        return f"Impossible de fermer {nom} : {e}"
