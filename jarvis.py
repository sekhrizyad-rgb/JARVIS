from intents import detect_intent
from skills.get_time import get_time
from skills.open_app import open_app
from skills.close_app import close_app
from skills.exit_jarvis import exit_jarvis
from skills.search_web import search_web


def process_command(commande):
    try:
        resultat = detect_intent(commande)
        intent = resultat["intent"]
        if intent == "GET_TIME":
            return get_time()
        elif intent == "OPEN_APP":
            return open_app(resultat["target"])
        elif intent == "CLOSE_APP":
            return close_app(resultat["target"])
        elif intent == "SEARCH_WEB":
            return search_web(resultat["query"])
        elif intent == "EXIT_JARVIS":
            exit_jarvis()
            return None
        elif intent == "UNKNOWN":
            return "Je ne connais pas encore cette commande."
        else:
            return f"Intent détecté : {resultat}"
    except Exception as e:
        return f"Une erreur est survenue, mais JARVIS continue : {e}"


def main():
    print("JARVIS est en ligne. Tape une commande.")
    while True:
        try:
            commande = input("> ")
        except (EOFError, KeyboardInterrupt):
            print("\nJARVIS s'arrête (interruption détectée).")
            break
        if commande.strip() == "":
            continue
        reponse = process_command(commande)
        if reponse is not None:
            print(reponse)


if __name__ == "__main__":
    main()
