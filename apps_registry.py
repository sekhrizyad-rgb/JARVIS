
import os


def _trouver_chrome():
    chemins_possibles = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(
            r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
        ),
    ]

    for chemin in chemins_possibles:
        if os.path.exists(chemin):
            return chemin

    return None


APPS = {
    "spotify": {
        "open_method": "uri",
        "open_value": "spotify:",
        "process_name": "Spotify.exe",
    },
    "chrome": {
        "open_method": "path",
        "open_value": _trouver_chrome(),
        "process_name": "chrome.exe",
    },
}

ALIASES = {
    "google chrome": "chrome",
}


def resolve_app(target):
    nom = ALIASES.get(target, target)
    return nom, APPS.get(nom)
