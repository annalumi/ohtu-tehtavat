class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        self.nationality = nationality
        players = self.reader.get_players()
        players_by_nationality = [p for p in players if p.nationality == self.nationality]
        players_by_nationality.sort(key=lambda x: x.goals + x.assists, reverse = True)

        return players_by_nationality