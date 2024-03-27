from lib.player import Player
# from lib.manager import Manager

class PlayerRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM players')
        players = []
        for row in rows:
            player = Player(row["id"], row["player_name"], row["player_position"],row["player_points"], row["player_goals_for"], row["player_goals_against"], )
            players.append(player)
        return players
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM players WHERE id = %s', [id])
        row = rows[0]
        return Player(row["id"], row["player_name"], row["player_points"], row["player_goals_for"], row["player_goals_against"])

# Has to use join table
    def find_manager_players(self, manager_id):
        rows = self._connection.execute("""SELECT players.id, players.player_name, players.player_position
                                        FROM managers_players 
                                        INNER JOIN players ON managers_players.player_id = players.id 
                                        WHERE managers_players.manager_id = %s""", [manager_id])
        players = []
        for row in rows:
            player = Player(row["id"], row["player_name"], row["player_position"], )
            players.append(player)
        return players

# Create has to also update managers_players table
    def create(self, player, manager_id):
        rows = self._connection.execute('INSERT INTO players (player_name, player_position) VALUES (%s, %s) RETURNING id',[player.player_name, player.player_position])
        row = rows[0]
        player.id = row["id"]
        self._connection.execute('INSERT INTO managers_players (manager_id, player_id) VALUES (%s, %s)', [manager_id, player.id])
        print(player.id)
        return player
    
# TODO This is behaving oddly!

    def create_squad_player(self, player, manager_id, squad_id):
        rows = self._connection.execute('INSERT INTO players (player_name, player_position) VALUES (%s, %s) RETURNING id',[player.player_name, player.player_position])
        row = rows[0]
        player.id = row["id"]
        self._connection.execute('INSERT INTO squads_players (squad_id, player_id) VALUES (%s, %s)', [squad_id, player.id])
        self._connection.execute('INSERT INTO managers_players (manager_id, player_id) VALUES (%s, %s)', [manager_id, player.id])
        return player
    
    def delete(self, id):
        rows = self._connection.execute('DELETE FROM players WHERE id = %s', [id])
        return None