players = []
def add_player():
    name = input("Enter player name: ")
    team = input("Enter team name: ")
    position = input("Enter position: ")
    players.append({"name": name, "team": team, "position": position})
    print(f"Player {name} added!")
def nba_players(team=None, position=None):
    search_player = players
    if team: 
        search_player = [player for player in search_player if player["team"] == team]
    if position:
        search_player = [player for player in search_player if player["position"] == position]
    return search_player
while True:
    choice = input("What is your choice: ")
    print("1. Add Player")
    print("2. Search Players")
    print("3. View All Players")
    print("4. Exit")

    if choice == "1":
        add_player()
    elif choice == "2":
        team = input("Enter team name: ")
        position = input("Enter position: ")
        nba_players(team, position)
        results = nba_players(team=team if team else None, position=position if position else None)
        if results:
            print("Filtered Players: ")
            for player in results:
                print(f"- {player['name']} ({player['team']}, {player['position']})")
        else:
            print("\nNo players match the criteria.")
    elif choice == "3":
        print("All players")
        for player in players:
            print(f"- {player['name']} ({player['team']}, {player['position']})")
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
