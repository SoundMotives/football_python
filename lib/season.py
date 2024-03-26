from lib.gameweek import GameWeek

class Season:
    def __init__(self, id=None, season_start_date=None, season_length=12, game_weeks=None, season_complete=False, squad_id=None) -> None:
        self.id = id 
        self.season_start_date = season_start_date
        self.season_length = season_length
        self.game_weeks = game_weeks or []
        self.season_complete = season_complete
        self.squad_id = squad_id

    def __repr__(self) -> str:
        return f"Season({self.id}, {self.season_start_date},{self.season_length})"
    
    def is_valid(self):
        # if self.id == None or self.id == "":
        #     return False
        if self.season_start_date == None or self.season_start_date == "":
            return False
        if self.season_length== None or self.season_length == "":
            return False
        return True

    def generate_errors(self):
        errors = []
        # if self.id == None or self.id == "":
        #     errors.append("ID can't be blank")
        if self.season_start_date == None or self.season_start_date == "":
            errors.append("Season start date can't be blank")
        if self.season_length == None or self.season_length == "":
            errors.append("Season length date can't be blank")   
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)
        
    def create_game_weeks(self, season_length):
        for i in range(1, season_length + 1):
            game_week = GameWeek(f"Week {i}")
            self.game_weeks.append(game_week)

    def check_season_completion(self):
        completed_game_weeks = sum(1 for game_week in self.game_weeks if game_week.availability_full)
        if completed_game_weeks >= 12:  # Assuming each game week has availability_full attribute
            self.season_complete = True
            print("Season complete!")