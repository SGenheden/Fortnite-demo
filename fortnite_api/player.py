
from .Client import Client


class FortnitePlayer:

    def __init__(self, username, platform="pc"):
        client = Client()
        stats = None
        self.name = username
        try:
            response = client.send_request(platform, username)
            stats = response[1]
        except:
            stats = None
        self.stats = stats
        if stats:
            self.score = int(stats[6]['value'].replace(",",""))
            self.wins = int(stats[8]['value'].replace(",",""))
            self.matches = int(stats[7]['value'].replace(",",""))
            self.kills = int(stats[10]['value'].replace(",",""))
