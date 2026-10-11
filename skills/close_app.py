import os
from apps_registry import APPS


def close_app(target):
    if target not in APPS:
        return f"Je ne connais pas l'application '{target}'."

    app = APPS[target]
    process = app["process_name"]

    result = os.system(f"taskkill /f /im {process}")

    if result == 0:
        return f"{target} fermé."
    else:
        return f"{target} n'était pas ouvert ou n'a pas pu être fermé."
