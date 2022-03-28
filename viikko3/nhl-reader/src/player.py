class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.nationality = player_dict["nationality"]
        self.assists = player_dict["assists"]
        self.goals = player_dict["goals"]
        self.team = player_dict["team"]
    
    def __str__(self):
        return (f"{self.name:20} {self.team:4} {str(self.assists):2} + {str(self.goals):2} = {str(self.assists+self.goals):2}")
