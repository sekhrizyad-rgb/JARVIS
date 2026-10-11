import unittest
from unittest.mock import patch
from skills.close_app import close_app


class TestCloseApp(unittest.TestCase):
    @patch("skills.close_app.resolve_app")
    @patch("skills.close_app.os.system")
    def test_close_app_succes(self, mock_system, mock_resolve):
        mock_resolve.return_value = ("spotify", {"process_name": "Spotify.exe"})
        mock_system.return_value = 0
        resultat = close_app("spotify")
        mock_system.assert_called_once_with("taskkill /im Spotify.exe")
        self.assertEqual(resultat, "Demande de fermeture envoyée à spotify.")

    @patch("skills.close_app.resolve_app")
    @patch("skills.close_app.os.system")
    def test_close_app_echec_sans_force(self, mock_system, mock_resolve):
        mock_resolve.return_value = ("spotify", {"process_name": "Spotify.exe"})
        mock_system.return_value = 128
        resultat = close_app("spotify")
        self.assertNotIn("/f", mock_system.call_args[0][0])
        self.assertIn("n'a pas pu", resultat)

    @patch("skills.close_app.resolve_app")
    def test_close_app_inconnue(self, mock_resolve):
        mock_resolve.return_value = ("minecraft", None)
        self.assertIn("ne connais pas", close_app("minecraft"))

    @patch("skills.close_app.resolve_app")
    @patch("skills.close_app.os.system", side_effect=OSError("boom"))
    def test_close_app_erreur_geree(self, mock_system, mock_resolve):
        mock_resolve.return_value = ("spotify", {"process_name": "Spotify.exe"})
        self.assertIn("Impossible de fermer", close_app("spotify"))
