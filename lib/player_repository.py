from lib.player import Player

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

    def create(self, player, manager_id):
        rows = self._connection.execute('INSERT INTO players (player_name, player_position) VALUES (%s, %s) RETURNING id',[player.player_name, player.player_position])
        row = rows[0]
        print(row)
        player.id = row["id"]
        print(player)
        self._connection.execute('INSERT INTO managers_players (manager_id, player_id) VALUES (%s, %s)', [manager_id, player.id])
        print(player.id)
        return player
    
    def delete(self, id):
        rows = self._connection.execute('DELETE FROM players WHERE id = %s', [id])
        return None