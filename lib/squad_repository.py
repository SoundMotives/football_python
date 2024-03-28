from lib.squad import Squad
from lib.player import Player

class SquadRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM squads')
        squads = []
        for row in rows:
            squad = Squad(row["squad_name"])
            # row["id"], 
            squads.append(squad)
        return squads

# Has to use join table
    def all_manager_squads(self, manager_id):
        rows = self._connection.execute("""SELECT squads.id, squads.squad_name
                                        FROM managers_squads 
                                        INNER JOIN squads ON managers_squads.squad_id = squads.id 
                                        WHERE managers_squads.manager_id = %s""", [manager_id])
        squads = []
        for row in rows:
            squad = Squad(row["squad_name"])
            # row["id"], 
            squads.append(squad)
        return squads
    
    def get_squad_players(self, squad_id):
        rows = self._connection.execute("""SELECT players.id, players.player_name, players.player_position, players.player_points, players.player_goals_for, players.player_goals_against 
                                        FROM squads_players 
                                        INNER JOIN players ON squads_players.player_id = players.id 
                                        WHERE squads_players.squad_id = %s""", [squad_id])
        squad_players = []
        for row in rows:
            player = Player(row["player_name"], row["player_position"], row["player_points"], row["player_goals_for"], row["player_goals_against"])
            # row["id"], 
            squad_players.append(player)
        return squad_players
        
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM squads WHERE id = %s', [id])
        row = rows[0]
        return Squad(row["squad_name"])
    # row["id"], 
    def find_squads_by_player_id(self, player_id):
        rows = self._connection.execute("""SELECT squads.id, squads.squad_name
                                        FROM squads_players 
                                        INNER JOIN squads ON squads_players.squad_id = squads.id 
                                        WHERE squads_players.player_id = %s""", [player_id])
        squads = []
        for row in rows:
            squad = Squad(row["squad_name"])
            # row["id"], 
            squads.append(squad)
        return squads
        

# Create has to also update managers_squads table
    def create(self, squad, manager_id):
        rows = self._connection.execute('INSERT INTO squads (squad_name) VALUES (%s) RETURNING id',[squad.squad_name])
        row = rows[0]
        squad.id = row["id"]
        self._connection.execute('INSERT INTO managers_squads (manager_id, squad_id) VALUES (%s, %s)', [manager_id, squad.id])
        return squad
    
    def delete(self, id):
        rows = self._connection.execute('DELETE FROM squads WHERE id = %s', [id])
        return None