import json
import requests

class Client:

    URL = 'https://api.fortnitetracker.com/v1/profile/'

    def send_request(self, platform, username):
        headers = {"TRN-Api-Key": "59dcc666-a140-4852-940f-5c31f0457241"}
        r = requests.get(self.URL + platform + '/' + username, headers=headers)
        response = r.json()

        try:
            player_data = response['stats']
            lifetime_stats = response['lifeTimeStats']
        except Exception:
            return ''

        return [player_data, lifetime_stats]
