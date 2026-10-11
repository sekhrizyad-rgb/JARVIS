import os
import subprocess
from apps_registry import APPS


def open_app(target):
    if target not in APPS:
        return f"Je ne connais pas l'application '{target}'."

    app = APPS[target]

    if app["open_method"] == "uri":
        os.startfile(app["open_value"])
        return f"{target} ouvert."

    if app["open_method"] == "path":
        subprocess.Popen(app["open_value"])
        return f"{target} ouvert."

    return f"Méthode d'ouverture inconnue pour '{target}'."
