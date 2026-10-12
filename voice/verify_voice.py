"""
Script de vérification isolé — NE FAIT PAS PARTIE du Core v0.2.
Objectif unique : confirmer que la clé API et le reference_id
fonctionnent avec le modèle s2.1-pro-free, avant toute intégration.
"""
import os
import sys
from pathlib import Path
import httpx
from dotenv import load_dotenv

DOSSIER_VOICE = Path(__file__).resolve().parent
RACINE_PROJET = DOSSIER_VOICE.parent

load_dotenv(RACINE_PROJET / ".env")

API_KEY = os.getenv("FISH_API_KEY")
REFERENCE_ID = "5edf9989f5d041d284194327f1234ee8"
MODELE = "s2.1-pro-free"  # jamais de bascule automatique vers un modèle payant
TIMEOUT_SECONDES = 20
FICHIER_SORTIE = DOSSIER_VOICE / "test_voix_jarvis.mp3"
TEXTE_TEST = (
    "[calm] Bonsoir, monsieur. Tous les systèmes sont opérationnels.\n"
    "[dryly] Et pour une fois, ce n'est pas qu'une façon de parler."
)


def verifier_cle():
    if not API_KEY:
        print("Erreur : FISH_API_KEY introuvable. Vérifie ton fichier .env à la racine du projet.")
        sys.exit(1)


def ressemble_a_un_mp3(contenu):
    """
    Vérifie la signature binaire plutôt que de se fier uniquement au
    Content-Type (qui peut être générique, type application/octet-stream).
    Un MP3 commence soit par un tag ID3v2 ('ID3'), soit directement par
    un en-tête de frame MPEG (0xFF suivi d'un octet dont les 3 premiers
    bits sont à 1).
    """
    if len(contenu) < 3:
        return False
    if contenu[:3] == b"ID3":
        return True
    if contenu[0] == 0xFF and (contenu[1] & 0xE0) == 0xE0:
        return True
    return False


def interpreter_erreur(statut, corps_reponse):
    messages = {
        401: "Clé API invalide, expirée, ou absente du .env.",
        403: (
            "Accès refusé. Cause non certaine : peut venir d'une clé sans les droits "
            "nécessaires, d'une restriction propre au modèle gratuit, ou d'un accès "
            "limité à ce reference_id. À vérifier sur le dashboard Fish Audio."
        ),
        404: (
            "Ressource introuvable. Cause non certaine : peut venir d'un reference_id "
            "mal copié, mais aussi d'une erreur d'URL ou d'un problème temporaire côté "
            "API. Ne pas conclure que la voix est invalide sans vérification manuelle."
        ),
        429: "Limite de débit ou quota atteint. Réessayer plus tard ou vérifier le compte.",
    }
    message = messages.get(statut, f"Statut inattendu : {statut}")
    print(f"Échec : {message}")
    print("Détail brut de la réponse (pour diagnostic) :")
    print(corps_reponse[:500])


def main():
    verifier_cle()
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "model": MODELE,
    }
    payload = {
        "text": TEXTE_TEST,
        "reference_id": REFERENCE_ID,
        "format": "mp3",
    }
    print(f"Appel à Fish Audio (modèle : {MODELE}, voix : {REFERENCE_ID[:8]}...)")
    try:
        reponse = httpx.post(
            "https://api.fish.audio/v1/tts",
            headers=headers,
            json=payload,
            timeout=TIMEOUT_SECONDES,
        )
    except httpx.TimeoutException:
        print(f"Échec : délai dépassé après {TIMEOUT_SECONDES} secondes.")
        sys.exit(1)
    except httpx.RequestError as e:
        print(f"Échec réseau : {e}")
        sys.exit(1)

    if reponse.status_code != 200:
        interpreter_erreur(reponse.status_code, reponse.text)
        sys.exit(1)

    if not ressemble_a_un_mp3(reponse.content):
        print(
            f"Échec : statut 200 reçu, mais le contenu ne ressemble pas à un MP3 valide "
            f"(taille : {len(reponse.content)} octets, Content-Type annoncé : "
            f"'{reponse.headers.get('content-type', 'absent')}')."
        )
        sys.exit(1)

    DOSSIER_VOICE.mkdir(parents=True, exist_ok=True)
    with open(FICHIER_SORTIE, "wb") as f:
        f.write(reponse.content)

    print(f"Succès. Audio enregistré : {FICHIER_SORTIE}")
    print("Écoute le fichier pour confirmer la voix, le ton et la prononciation française.")


if __name__ == "__main__":
    main()
