import unittest
from unittest.mock import patch
import jarvis


class TestProcessCommand(unittest.TestCase):
    @patch("jarvis.get_time", return_value="Il est 10h00.")
    def test_process_command_get_time(self, mock_get_time):
        self.assertEqual(jarvis.process_command("quelle heure"), "Il est 10h00.")

    @patch("jarvis.open_app", side_effect=Exception("panne simulee"))
    def test_process_command_capture_exception_skill(self, mock_open_app):
        resultat = jarvis.process_command("ouvre spotify")
        self.assertIn("Une erreur est survenue", resultat)
        self.assertIn("panne simulee", resultat)

    @patch("jarvis.detect_intent", side_effect=Exception("detection cassee"))
    def test_process_command_capture_exception_detection(self, mock_detect):
        resultat = jarvis.process_command("commande quelconque")
        self.assertIn("Une erreur est survenue", resultat)
        self.assertIn("detection cassee", resultat)

    def test_process_command_unknown(self):
        self.assertEqual(jarvis.process_command("fais moi voler"), "Je ne connais pas encore cette commande.")


class TestMainLoopArret(unittest.TestCase):
    @patch("builtins.input", side_effect=EOFError)
    @patch("builtins.print")
    def test_main_arret_sur_eof(self, mock_print, mock_input):
        jarvis.main()
        mock_input.assert_called_once()

    @patch("builtins.input", side_effect=KeyboardInterrupt)
    @patch("builtins.print")
    def test_main_arret_sur_keyboard_interrupt(self, mock_print, mock_input):
        jarvis.main()
        mock_input.assert_called_once()
