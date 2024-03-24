from lib.player import Player
# from lib.gameweek import GameWeek

class GameResult:
    def __init__(self, black_team_list, white_team_list):
        self.black_team_list = black_team_list
        self.white_team_list = white_team_list   
        self.final_score = {"black_team": 0, "white_team": 0}
        self.winning_team = None

    def record_goals(self, black_team_goals, white_team_goals):
        self.final_score["black_team"] = int(black_team_goals) if black_team_goals else 0
        self.final_score["white_team"] = int(white_team_goals) if white_team_goals else 0

    def calculate_game_points(self):
        if self.final_score["black_team"] > self.final_score["white_team"]:
            self.winning_team = "black_team"
        elif self.final_score["black_team"] < self.final_score["white_team"]:
            self.winning_team = "white_team"
        else:
            pass
        # return self.winning_team
        
    def assign_player_points(self):
        if self.winning_team ==  "black_team":
            for player in self.black_team_list:
                player.player_points += 3
                player.player_goals_for += int(self.final_score["black_team"])
                player.player_goals_against += int(self.final_score["white_team"])
        elif self.winning_team ==  "white_team":
            for player in self.white_team_list:
                player.player_points += 3
                player.player_goals_for += int(self.final_score["white_team"])
                player.player_goals_against += int(self.final_score["black_team"])
        else:
            for player in self.black_team_list:
                player.player_points += 1
                player.player_goals_for += int(self.final_score["black_team"])
                player.player_goals_against += int(self.final_score["white_team"])

            for player in self.white_team_list:
                player.player_points += 1
                player.player_goals_for += int(self.final_score["black_team"])
                player.player_goals_against += int(self.final_score["white_team"])






