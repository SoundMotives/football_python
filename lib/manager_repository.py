from lib.manager import Manager

class ManagerRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM managers')
        managers = []
        for row in rows:
            manager = Manager(row["id"], row["manager_name"], row["manager_email"])
            managers.append(manager)
        return managers
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM managers WHERE id = %s', [id])
        row = rows[0]
        return Manager(row["id"], row["manager_name"], row["manager_email"])

    def create(self, manager):
        rows = self._connection.execute('INSERT INTO managers (manager_name, manager_email) VALUES (%s, %s) RETURNING id',[manager.manager_name, manager.manager_email])
        row = rows[0]
        manager.id = row["id"]
        return manager
    
    def delete(self, id):
        rows = self._connection.execute('DELETE FROM managers WHERE id = %s', [id])
        return None