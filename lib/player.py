class Player:
    def __init__(self, player_id, player_name, ):
        self.player_id = player_id
        self.player_name = player_name
        self.player_points = 0
        self.player_goals_for = 0
        self.player_goals_against = 0
        # self.player_goal_difference = 
        # self.player_position = player_position

    @property
    def player_goal_difference(self):
        return self.player_goals_for - self.player_goals_against

    def __eq__(self, other: object) -> bool:
        return self.__dict__ == other.__dict__
    
    def __repr__(self) -> str:
        return f"Player({self.player_id}, {self.player_name}, {self.player_points})"
    

