import random
from lib.player import Player
from lib.gameresult import GameResult

class GameWeek:
    def __init__(self, id=None, week_number="", game_week_date=None, availability_full=False, black_team_list=None, white_team_list=None, game_result=None) -> None:
        self.id = id 
        self.week_number = week_number
        self.game_week_date = game_week_date
        self.availability_full = availability_full
        self.black_team_list = black_team_list if black_team_list is not None else []
        self.white_team_list = white_team_list if white_team_list is not None else []
        self.game_result = game_result
        # self.final_score = {self.black_team: None, self.white_team: None}

    def __repr__(self) -> str:  
        return f"GameWeek({self.week_number}, Available_players={self.available_players}, availability_full={self.availability_full}, Black_team={self.black_team_list}, White_team={self.white_team_list})"      
    
    def is_valid(self):
        # if self.id == None or self.id == "":
        #     return False
        if self.week_number == None or self.week_number == "":
            return False
        return True

    def generate_errors(self):
        errors = []
        # if self.id == None or self.id == "":
        #     errors.append("ID can't be blank")
        if self.week_number == None or self.week_number == "":
            errors.append("Week number can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)

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

    

