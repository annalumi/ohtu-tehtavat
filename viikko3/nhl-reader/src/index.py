import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"

    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'], 
            player_dict['nationality'], 
            player_dict["assists"],
            player_dict["goals"],
            player_dict["team"]
        )

        players.append(player)

    print("Players from FIN:")

    for player in players:
        if player.nationality == "FIN":
            total = player.assists + player.goals
            print (f"{player.name:20} {player.team:4} {str(player.assists):2} + {str(player.goals):2} = {str(total):2}")

if __name__ == "__main__":
    main()