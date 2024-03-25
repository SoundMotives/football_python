class Player:
    def __init__(self, id, player_name, player_position, player_points=0, player_goals_for=0, player_goals_against=0):
        self.id = id
        self.player_name = player_name
        self.player_position = player_position
        self.player_points = player_points
        self.player_goals_for = player_goals_for
        self.player_goals_against = player_goals_against
        # self.player_goal_difference = 

    @property
    def player_goal_difference(self):
        return self.player_goals_for - self.player_goals_against

    def __eq__(self, other: object) -> bool:
        return self.__dict__ == other.__dict__
    
    def __repr__(self) -> str:
        return f"Player({self.id}, {self.player_name}, {self.player_position}, {self.player_points})"
    

    def generate_errors(self):
        errors = []
        if self.player_name == None or self.player_name == "":
            errors.append("Name can't be blank")
        if self.player_position == None or self.player_position == "":
            errors.append("Position can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)
        
    def is_valid(self):
        if self.player_name == None or self.player_name == "":
            return False
        if self.player_position == None or self.player_position == "":
            return False
        return True
