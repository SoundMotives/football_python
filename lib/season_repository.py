from lib.season import Season

class SeasonRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM seasons')
        seasons = []
        for row in rows:
            season = Season(row["id"], row["season_start_date"], row["season_length"], row["game_weeks"], row["season_complete"], row["squad_id"])
            seasons.append(season)
        return seasons

    def single_squad_all_seasons(self, squad_id):
        rows = self._connection.execute('SELECT * FROM seasons WHERE squad_id = %s', [squad_id])
        seasons = []
        for row in rows:
            season = Season(row["id"], row["season_start_date"], row["season_length"], row["game_weeks"], row["season_complete"], row["squad_id"] )
            seasons.append(season)
        return seasons
    
    def multiple_squads_all_seasons(self, squads):
        seasons = [] 
        for squad in squads:
            rows = self._connection.execute("""SELECT seasons. *, squads.squad_name 
                                            FROM seasons 
                                            JOIN squads ON seasons.squad_id = squads.id 
                                            WHERE squad_id = %s""", [squad.id])
            for row in rows:
                season = Season(row["id"], row["season_start_date"], row["season_length"], row["game_weeks"], row["season_complete"], row["squad_id"] )
                season.squad_name = row["squad_name"]
                seasons.append(season)
        return seasons
    
    #  TRYING TO POPULATE THE SEASONS FIELD IN PLAYER CREATION - BASED ONLY ON MANAGER      
    def manager_all_seasons(self, manager_id):
        seasons = [] 
        rows = self._connection.execute("""SELECT seasons. *, squads.squad_name 
                                        FROM seasons 
                                        JOIN squads ON seasons.squad_id = squads.id 
                                        JOIN managers_squads ON squads.id = managers_squads.squad_id
                                        WHERE managers_squads.manager_id = %s""", [manager_id])
        for row in rows:
            season = Season(row["id"],row["season_start_date"], row["season_length"], row["game_weeks"], row["season_complete"], row["squad_id"] )  
            season.squad_name = row["squad_name"]
            seasons.append(season)
        return seasons

    def find(self, id):
        rows = self._connection.execute('SELECT * FROM seasons WHERE id = %s', [id])
        row = rows[0]
        return Season(row["id"], row["season_start_date"], row["season_length"], row["game_weeks"], row["season_complete"], row["squad_id"] )

#TODO Why does this look so different?
# Create has to also update managers_players table
    def create(self, season, squad_id):
        if season.id is None:
            rows = self._connection.execute('INSERT INTO seasons (season_start_date, season_length, squad_id) VALUES (%s, %s, %s) RETURNING id',[season.season_start_date, season.season_length, squad_id])
            row = rows[0]
            season.id = row["id"]       
        return season
        # else:
        #     pass
    
    def delete(self, id):
        rows = self._connection.execute('DELETE FROM seasons WHERE id = %s', [id])
        return None