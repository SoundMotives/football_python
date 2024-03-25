from lib.squad import Squad

class SquadRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM squads')
        squads = []
        for row in rows:
            squad = Squad(row["id"], row["squad_name"])
            squads.append(squad)
        return squads
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM squads WHERE id = %s', [id])
        row = rows[0]
        return Squad(row["id"], row["squad_name"])

    def create(self, squad):
        rows = self._connection.execute('INSERT INTO squads (squad_name) VALUES (%s) RETURNING id',[squad.squad_name])
        row = rows[0]
        squad.id = row["id"]
        return squad
    
    def delete(self, id):
        rows = self._connection.execute('DELETE FROM squads WHERE id = %s', [id])
        return None