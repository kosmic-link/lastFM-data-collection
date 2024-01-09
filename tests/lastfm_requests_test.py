import os
import unittest
from dotenv import load_dotenv
from src.lastfm_requests import LastFMConnection



class LastFMConnectionTests(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        api_key = os.getenv('LASTFM_API_KEY')
        api_secret = os.getenv('LASTFM_API_SECRET')
        self.lastfm_connection = LastFMConnection(api_key, api_secret)

    def testLibraryArtists(self):
        cardoor_libary_artists = self.lastfm_connection.get_user_artists("Car_door", limit=10)
        self.assertEqual(len(cardoor_libary_artists["artists"]["artist"]), 10)
