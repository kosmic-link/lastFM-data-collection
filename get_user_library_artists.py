import pylast
import csv
import sys
import os

def get_lastfm_library(api_key, api_secret, username, password_hash):
    network = pylast.LastFMNetwork(api_key=api_key, api_secret=api_secret,
                                   username=username, password_hash=password_hash)

    user = network.get_user(username)
    library = user.get_library()

    artists_data = []

    for item in library.get_items():
        artist = item.get_artist()
        artist_info = artist.get_info()

        artist_data = {
            'name': artist.get_name(),
            'playcount': artist_info.get_playcount(),
            'listeners': artist_info.get_listener_count(),
            'url': artist_info.get_url(),
        }

        artists_data.append(artist_data)

    return artists_data

def save_to_csv(data, filename='lastfm_library.csv'):
    keys = data[0].keys()
    with open(filename, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, keys)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python lastfm_script.py <lastfm_username>")
        sys.exit(1)

    username = sys.argv[1]

    # Replace these with your own Last.fm API credentials
    API_KEY = "YOUR_API_KEY"
    API_SECRET = "YOUR_API_SECRET"

    # Replace these with your own Last.fm account credentials
    PASSWORD = "YOUR_PASSWORD"
    PASSWORD_HASH = pylast.md5(PASSWORD)

    artists_data = get_lastfm_library(os.getenv("LAST"), API_SECRET, username, PASSWORD_HASH)
    save_to_csv(artists_data)
