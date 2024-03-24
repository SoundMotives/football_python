from lib.gameweek import GameWeek

class Season:
    def __init__(self, season_number) -> None:
        self.season_number = season_number
        self.game_weeks = []
        self.season_complete = False

    def __repr__(self) -> str:
        return f"Season({self.season_number})"

    def create_game_weeks(self, season_length=12):
        for i in range(1, season_length + 1):
            game_week = GameWeek(f"Week {i}")
            self.game_weeks.append(game_week)

    def check_season_completion(self):
        completed_game_weeks = sum(1 for game_week in self.game_weeks if game_week.spots_full)
        if completed_game_weeks >= 12:  # Assuming each game week has spots_full attribute
            self.season_complete = True
            print("Season complete!")