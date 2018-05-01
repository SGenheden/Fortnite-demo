
from Client import Client


class FortnitePlayer:

    def __init__(self, username, platform="pc"):
        client = Client()
        stats = None
        try:
            response = client.send_request(platform, username)
            stats = response[2]
        except:
            stats = None
        if stats:
            self.score = int(stats[6]['Value'].replace(",",""))
            self.wins = int(stats[8]['Value'].replace(",",""))
            self.matches = int(stats[7]['Value'].replace(",",""))
            self.kills = int(stats[10]['Value'].replace(",",""))
