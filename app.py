import os
from flask import Flask, request, redirect, render_template
from lib.database_connection import get_flask_database_connection
from lib.manager_repository import ManagerRepository
from lib.manager import Manager
from lib.squad_repository import SquadRepository
from lib.squad import Squad
from lib.player_repository import PlayerRepository
from lib.player import Player
from lib.season_repository import SeasonRepository
from lib.season import Season
from lib.gameweek_repository import GameWeekRepository
from lib.gameweek import GameWeek

# Create a new Flask app
app = Flask(__name__)

# DISPLAY HOME PAGE
@app.route('/home', methods=['GET'])
def welcome():
    return render_template('landing_page.html')

# DISPLAY MANAGER CREATION PAGE // CREATE MANAGER
@app.route('/managers', methods=["GET", 'POST'])
def create_manager():
    connection = get_flask_database_connection(app)
    repository = ManagerRepository(connection)
    if request.method == 'POST':
        manager_name = request.form['manager_name']
        manager_email = request.form['manager_email']
        manager = Manager(None, manager_name, manager_email)
        if not manager.is_valid():
            return render_template('managers/new.html', manager=manager, errors=manager.generate_errors()), 400
        manager = repository.create(manager)
        return redirect(f"/managers/{manager.id}")
    else:
        return render_template('managers/new.html')

# DISPLAY MAIN MANAGER PAGE
@app.route('/managers/<int:id>', methods=['GET', 'POST'])
def get_manager(id):
    connection = get_flask_database_connection(app)
    manager_repository = ManagerRepository(connection)
    squad_repository = SquadRepository(connection)
    player_repository = PlayerRepository(connection)
    season_repository = SeasonRepository(connection)
    manager = manager_repository.find(id)
    if request.method == 'POST':   
        if manager is None:
            abort(404)
            return render_template('managers/edit.html', manager=manager)
    # finding squds that match manager
    squads = squad_repository.find_manager_squads(id)
    players = player_repository.find_manager_players(id)    
    return render_template('managers/show.html', manager=manager, squads=squads, players=players)

#  DISPLAY SQUAD CREATION PAGE // CREATE SQUAD
@app.route('/managers/<int:id>/squads', methods=['GET', 'POST'])
def create_squad(id):
    connection = get_flask_database_connection(app)
    manager_repository = ManagerRepository(connection)
    squad_repository = SquadRepository(connection)
    manager = manager_repository.find(id)
    manager_id = manager.id
    if manager is None:
        return "Manager not found", 404
    if request.method == 'POST':
        squad_name = request.form['squad_name']
        squad = Squad(None, squad_name)
        if not squad.is_valid():
            return render_template('squads/new.html', manager=manager, errors=squad.generate_errors()), 400
        squad_repository.create(squad, manager_id)
        return redirect(f"/managers/{manager.id}")
    return render_template('squads/new.html', manager=manager)

# DISPLAY A SINGLE SQUAD PAGE
@app.route('/managers/<int:manager_id>/squads/<int:squad_id>', methods=['GET', 'POST'])
def get_squad(manager_id, squad_id):
    connection = get_flask_database_connection(app)
    manager_repository = ManagerRepository(connection)
    squad_repository = SquadRepository(connection)   
    season_repository = SeasonRepository(connection)
    manager = manager_repository.find(manager_id)
    squad = squad_repository.find(squad_id)
    seasons = season_repository.all_squad_seasons(squad_id)
    if request.method == 'POST':   
        if manager is None:
            abort(404)
            return render_template('managers/edit.html', manager=manager)    
    return render_template('squads/show.html', manager=manager, squad=squad, seasons=seasons)


# DISPLAY PLAYER CREATION PAGE // CREATE PLAYER
@app.route('/managers/<int:manager_id>/players/', methods=['GET', 'POST'])
def create_player(manager_id):
    connection = get_flask_database_connection(app)
    manager_repository = ManagerRepository(connection)
    player_repository = PlayerRepository(connection)
    manager = manager_repository.find(manager_id)
    if manager is None:
        return "Manager not found", 404
    if request.method == 'POST':
        player_name = request.form['player_name']
        player_position = request.form['player_position']
        player = Player(None, player_name, player_position)
        if not player.is_valid():
            players = player_repository.all()
            return render_template('players/new.html', manager=manager, players=players, errors=player.generate_errors()), 400
        player_repository.create(player, manager_id)
        return redirect(f"/managers/{manager.id}/players/")
    else:
        players = player_repository.all()
        return render_template('players/new.html', manager=manager, players=players)



#  DISPLAY SEASON CREATION PAGE // CREATE SEASON
@app.route('/managers/<int:manager_id>/squads/<int:squad_id>/seasons', methods=['GET', 'POST'])
def create_season(manager_id, squad_id):
    connection = get_flask_database_connection(app)
    manager_repository = ManagerRepository(connection)
    squad_repository = SquadRepository(connection)
    season_repository = SeasonRepository(connection)
    gameweek_repository = GameWeekRepository(connection)
    manager = manager_repository.find(manager_id)
    # manager_id = manager.id
    if manager is None:
        return "Manager not found", 404
    squad = squad_repository.find(squad_id)
    if squad is None:
        return "Squad not found", 404
    if request.method == 'POST':
        season_start_date = request.form['season_start_date']
        season_length = request.form['season_length']
        # game_weeks = request.form['game_weeks']
        # season_complete = request.form['season_complete']

        season = Season(None, season_start_date, season_length) #, game_weeks, season_complete
        if not season.is_valid():
            return render_template('seasons/new.html', manager=manager, squad=squad, errors=season.generate_errors()), 400
        season_repository.create(season, squad_id)
        gameweek_repository.create_gameweeks_for_season(season)
        return redirect(f"/managers/{manager_id}/squads/{squad_id}")
    return render_template('seasons/new.html', manager=manager, squad=squad)



# DISPLAY A SINGLE SEASON PAGE
@app.route('/managers/<int:manager_id>/squads/<int:squad_id>/seasons/<int:season_id>', methods=['GET', 'POST'])
def get_season(manager_id, squad_id, season_id):
    connection = get_flask_database_connection(app)
    manager_repository = ManagerRepository(connection)
    squad_repository = SquadRepository(connection)   
    season_repository = SeasonRepository(connection)
    gameweek_repository = GameWeekRepository(connection)
    manager = manager_repository.find(manager_id)
    squad = squad_repository.find(squad_id)
    season = season_repository.find(season_id)
    if request.method == 'POST':   
        if manager is None:
            abort(404)
            return render_template('managers/edit.html', manager=manager)
    gameweeks = gameweek_repository.all_season_gameweeks(season_id)    
    return render_template('seasons/show.html', manager=manager, squad=squad, season=season, gameweeks=gameweeks)


# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
