
import os
import subprocess
from apps_registry import resolve_app


def open_app(target):
    nom, app = resolve_app(target)

    if app is None:
        return f"Je ne connais pas l'application '{target}'."

    try:
        if app["open_method"] == "uri":
            os.startfile(app["open_value"])
            return f"{nom} ouvert."

        if app["open_method"] == "path":
            if not app["open_value"]:
                return f"Chemin introuvable pour '{nom}' sur ce PC."

            subprocess.Popen(app["open_value"])
            return f"{nom} ouvert."

        return f"Méthode d'ouverture inconnue pour '{nom}'."

    except Exception as e:
        return f"Impossible d'ouvrir {nom} : {e}"
