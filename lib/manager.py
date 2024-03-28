from lib.squad import Squad 
from lib.player import Player

class Manager:
    def __init__(self, manager_name="", manager_email=""):
        # self.id = id id=None,
        self.manager_name = manager_name
        self.manager_email = manager_email
        # self.squads = squads or []
        # self.players = players or []

    def __eq__(self, other) -> bool:
        return self.__dict__ == other.__dict__
    
    def __repr__(self) -> str:
        return f"Manager({self.id}, {self.manager_name}, {self.manager_email})"    
   
    def is_valid(self):
        # if self.id == None or self.id == "":
        #     return False
        if self.manager_name == None or self.manager_name == "":
            return False
        if self.manager_email == None or self.manager_email == "":
            return False
        return True

    def generate_errors(self):
        errors = []
        if self.manager_name == None or self.manager_name == "":
            errors.append("Name can't be blank")
        if self.manager_email == None or self.manager_email == "":
            errors.append("Email can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)

    def create_squad(self, squad_name):
        squad = Squad(squad_name)
        self.squads.append(squad)
        return squad
    
    def create_player(self, player_id, player_name):
        player = Player(player_id, player_name)
        self.players.append(player)
        return player

