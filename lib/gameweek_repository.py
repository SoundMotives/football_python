from datetime import datetime, timedelta
from lib.gameweek import GameWeek

class GameWeekRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_gameweeks_for_season(self, season):
        season_start_date = datetime.strptime(season.season_start_date, '%Y-%m-%d')
        for week_number in range(1, int(season.season_length) + 1):
            game_week_date = season_start_date + timedelta(weeks=(week_number -1))
            self._connection.execute('INSERT INTO game_weeks (game_week_date, week_number, season_id) VALUES (%s, %s, %s)',[game_week_date, week_number, season.id])

    def find(self, id):
        rows = self._connection.execute('SELECT * FROM game_weeks WHERE id = %s', [id])
        row = rows[0]
        return GameWeek(row["week_number"], row["game_week_date"], row["availability_full"], row["black_team_list"], row["white_team_list"], row["game_result"])
# row["id"], 

    def all_season_gameweeks(self, season_id):
        rows = self._connection.execute('SELECT * FROM game_weeks WHERE season_id = %s', [season_id])
        gameweeks = []
        for row in rows:
            gameweek = GameWeek(row["week_number"], row["game_week_date"], row["availability_full"], row["black_team_list"], row["white_team_list"], row["game_result"])
# row["id"], 
            gameweeks.append(gameweek)
        return gameweeks