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

# Has to use join table
    def find_manager_squads(self, manager_id):
        rows = self._connection.execute("""SELECT squads.id, squads.squad_name
                                        FROM managers_squads 
                                        INNER JOIN squads ON managers_squads.squad_id = squads.id 
                                        WHERE managers_squads.manager_id = %s""", [manager_id])
        squads = []
        for row in rows:
            squad = Squad(row["id"], row["squad_name"])
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