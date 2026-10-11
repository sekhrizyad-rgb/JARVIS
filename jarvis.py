from intents import detect_intent
from skills.get_time import get_time
from skills.open_app import open_app
from skills.close_app import close_app
from skills.exit_jarvis import exit_jarvis
from skills.search_web import search_web


def main():
    print("JARVIS est en ligne. Tape une commande.")

    while True:
        commande = input("> ")

        if commande.strip() == "":
            continue

        resultat = detect_intent(commande)
        intent = resultat["intent"]

        if intent == "GET_TIME":
            reponse = get_time()
            print(reponse)
        elif intent == "OPEN_APP":
            target = resultat["target"]
            reponse = open_app(target)
            print(reponse)
        elif intent == "CLOSE_APP":
            target = resultat["target"]
            reponse = close_app(target)
            print(reponse)
        elif intent == "SEARCH_WEB":
            query = resultat["query"]
            reponse = search_web(query)
            print(reponse)
        elif intent == "EXIT_JARVIS":
            exit_jarvis()
        elif intent == "UNKNOWN":
            print("Je ne connais pas encore cette commande.")
        else:
            print(f"Intent détecté : {resultat}")


if __name__ == "__main__":
    main()
