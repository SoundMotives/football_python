import random
from lib.player import Player
from lib.gameresult import GameResult

class GameWeek:
    def __init__(self, week_number) -> None:
        self.week_number = week_number
        self.available_players =  []
        self.availability_full = False
        self.black_team_list = []
        self.white_team_list = []
        self.game_result = None
        # self.final_score = {self.black_team: None, self.white_team: None}

    def __repr__(self) -> str:  
        return f"GameWeek({self.week_number}, \nAvailable_players={self.available_players}, \navailability_full={self.availability_full}, \nBlack_team={self.black_team_list}, \nWhite_team={self.white_team_list})"      
    
    def ask_availability(self, squad):
        for player in squad.players:
            availability = input(f"Is {player.player_name} available for GameWeek {self.week_number}? (yes/no): ").lower()
            if availability != 'no':
                self.available_players.append(player)

    def assign_teams(self):
        random.shuffle(self.available_players)
        half = len(self.available_players) // 2
        self.black_team_list = self.available_players[:half]
        self.white_team_list = self.available_players[half:]

    def instantiate_game_result(self):
        self.game_result = GameResult(self.black_team_list, self.white_team_list)
        # self.game_result = game_result
        # return game_result

    

