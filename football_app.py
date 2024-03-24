from lib.manager import Manager
from lib.squad import Squad
from lib.season import Season
from lib.player import Player
from lib.gameweek import GameWeek
from lib.gameresult import GameResult

# create manager
manager = Manager("Dave The Manager", "dave@soundmotives.net")
print(manager.manager_name)
print(manager.manager_email)

#create squad
manager.create_squad("Shacklewell Sharks")
squad = manager.squads[0]
print(squad.squad_name)

# create players
manager.create_player(1, "Santi")
manager.create_player(2, "Tim")
manager.create_player(3, "Rob")
manager.create_player(4, "San")
manager.create_player(5, "Lee")
manager.create_player(6, "Kieran")
manager.create_player(7, "Drew")
manager.create_player(8, "George")
manager.create_player(9, "Seb")
manager.create_player(10, "David")
manager.create_player(11, "Dave")
manager.create_player(12, "Jack")
manager.create_player(13, "Carlos")
manager.create_player(14, "Lewis")

# add players to sqaud
for player in manager.players:
    squad.players.append(player)
print(f"Squad = {squad.players}")

#create a season
squad.create_season(1)
season = squad.seasons[0]
print(season)

#create gameweeks for season
season.create_game_weeks()
print(season.game_weeks)

# Availability for game_week
for gameweek in season.game_weeks:
    gameweek.ask_availability(squad)
    print(gameweek.available_players)
    if len(gameweek.available_players) == 14:
        gameweek.availability_full = True
    if gameweek.availability_full == True:
        gameweek.assign_teams()
    print(gameweek)

    gameweek.instantiate_game_result()
    gameresult = gameweek.game_result
    black_team_goals = input(f"How many goals did black team score?")
    white_team_goals = input(f"How many goals did white team score?")
    gameresult.record_goals(black_team_goals, white_team_goals)
    gameresult.calculate_game_points()
    gameresult.assign_player_points()
    sorted_players = sorted(manager.players, key=lambda player: player.player_points, reverse=True)
    for player in sorted_players:
        print(player)
    season.check_season_completion()
    if season.season_complete == True:
        print(f"Most Valuable Player: {sorted_players[0].player_name} with {sorted_players[0].player_points} player points!")
        print(f"Wood Spoon Player: {sorted_players[-1].player_name} with {sorted_players[-1].player_points} player points!")
        sorted_players = sorted(manager.players, key=lambda player: player.player_goals_for, reverse=True)
        print(f"Goal Machine: {sorted_players[0].player_name} with {sorted_players[0].player_goals_for} goals scored!")
        print(f"Goal Slouch: {sorted_players[-1].player_name} with {sorted_players[-1].player_goals_for} goals scored!")
        sorted_players = sorted(manager.players, key=lambda player: player.player_goals_against, reverse=True)
        print(f"Defensive liability: {sorted_players[0].player_name} with {sorted_players[0].player_goals_against} goals conceded!")
        print(f"Defensive Beast!: {sorted_players[-1].player_name} with {sorted_players[-1].player_goals_against} goals conceded!")
        for player in manager.players:
            _ = player.player_goal_difference
        sorted_players = sorted(manager.players, key=lambda player: player.player_goal_difference, reverse=True)
        print(f"Statistical Beast!: {sorted_players[0].player_name} with {sorted_players[0].player_goal_difference} goal aggregate!")
        print(f"Statistical Wimp!: {sorted_players[-1].player_name} with {sorted_players[-1].player_goal_difference} goal aggregate!")


# gameresult.










# for i in range(10):
#     player = Player(i, "Gary" + str(i))
#     squad1.append(player + str(i))
# print(squad1)
# for player in squad1:
#     print(player)
    