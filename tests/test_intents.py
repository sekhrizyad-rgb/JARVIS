import unittest
from intents import detect_intent


class TestDetectIntent(unittest.TestCase):
    def test_open_app(self):
        self.assertEqual(detect_intent("ouvre spotify"), {"intent": "OPEN_APP", "target": "spotify"})

    def test_open_app_multimot(self):
        self.assertEqual(detect_intent("ouvre google chrome"), {"intent": "OPEN_APP", "target": "google chrome"})

    def test_close_app(self):
        self.assertEqual(detect_intent("ferme chrome"), {"intent": "CLOSE_APP", "target": "chrome"})

    def test_exit(self):
        self.assertEqual(detect_intent("quitte"), {"intent": "EXIT_JARVIS"})

    def test_get_time(self):
        self.assertEqual(detect_intent("quelle heure"), {"intent": "GET_TIME"})

    def test_search(self):
        self.assertEqual(detect_intent("cherche insuffisance cardiaque"), {"intent": "SEARCH_WEB", "query": "insuffisance cardiaque"})

    def test_unknown(self):
        self.assertEqual(detect_intent("fais moi voler"), {"intent": "UNKNOWN"})

    def test_vide(self):
        self.assertEqual(detect_intent(""), {"intent": "UNKNOWN"})
