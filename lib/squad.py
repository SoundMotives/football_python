from .season import Season

class Squad:
    def __init__(self, squad_name):
        self.squad_name = squad_name
        self.players = []
        self.seasons = []

    def __eq__(self, other) -> bool:
        return self.__dict__ == other.__dict__
    
    def __repr__(self) -> str:
        return f"Squad({self.squad_name}, {self.players}, {self.seasons})"    

    def add_player(self, player):
        self.players.append(player)

    def create_season(self, season_number):
        season = Season(season_number)
        self.seasons.append(season)
        return season
