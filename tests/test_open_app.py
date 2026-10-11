import unittest
from unittest.mock import patch
from skills.open_app import open_app


class TestOpenApp(unittest.TestCase):
    @patch("skills.open_app.resolve_app")
    @patch("skills.open_app.os.startfile", create=True)
    def test_open_app_uri(self, mock_startfile, mock_resolve):
        mock_resolve.return_value = ("spotify", {"open_method": "uri", "open_value": "spotify:", "process_name": "Spotify.exe"})
        resultat = open_app("spotify")
        mock_startfile.assert_called_once_with("spotify:")
        self.assertEqual(resultat, "spotify ouvert.")

    @patch("skills.open_app.resolve_app")
    @patch("skills.open_app.subprocess.Popen")
    def test_open_app_path(self, mock_popen, mock_resolve):
        mock_resolve.return_value = ("chrome", {"open_method": "path", "open_value": r"C:\fake\chrome.exe", "process_name": "chrome.exe"})
        resultat = open_app("chrome")
        mock_popen.assert_called_once_with(r"C:\fake\chrome.exe")
        self.assertEqual(resultat, "chrome ouvert.")

    @patch("skills.open_app.resolve_app")
    def test_open_app_chemin_introuvable(self, mock_resolve):
        mock_resolve.return_value = ("chrome", {"open_method": "path", "open_value": None, "process_name": "chrome.exe"})
        self.assertIn("introuvable", open_app("chrome"))

    @patch("skills.open_app.resolve_app")
    def test_open_app_inconnue(self, mock_resolve):
        mock_resolve.return_value = ("minecraft", None)
        self.assertIn("ne connais pas", open_app("minecraft"))

    @patch("skills.open_app.resolve_app")
    @patch("skills.open_app.os.startfile", side_effect=OSError("boom"), create=True)
    def test_open_app_erreur_geree(self, mock_startfile, mock_resolve):
        mock_resolve.return_value = ("spotify", {"open_method": "uri", "open_value": "spotify:", "process_name": "Spotify.exe"})
        self.assertIn("Impossible d'ouvrir", open_app("spotify"))
