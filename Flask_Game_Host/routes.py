from Flask_Game_Host import app
from flask import redirect, render_template, url_for
from Flask_Game_Host.html_generator import fill_grid, fill_grid_from_db
from Flask_Game_Host.player import Player
from Flask_Game_Host.game import Game
from Flask_Game_Host.forms import GameForm
import sys 
sys.dont_write_bytecode = True
from flask import jsonify, request, Blueprint
from .mongo_config import mongo
from datetime import datetime

#temporary list of scores
top_players = [Player("Sam", 500), Player("Jeff", 2), Player("Sally", 1000), Player("Ryan", 50), Player("Lindsay", 750)]
#temporary list of game titles to use for scoreboard
game_titles = [Game("Chess"), Game("Pinball")]
#calling class method to sort scores
top_players = Player.sort_players(top_players)


routes_app = Blueprint('routes', __name__)

def build_leaderboard_html():
  html_string = "<table class=\"leaderboard\"><caption><h4>" 
  html_string += game_titles[0].title + " Scoreboard</h4></caption><tr><th>Username</th><th>Score</th></tr>"
  for obj in top_players:
    html_string += "<tr><td>" + obj.username + "</td>"
    html_string += "<td>" + str(obj.score) + "</td></tr>"
  html_string += "</table>"
  return html_string



@app.route('/')
@app.route('/home')
def homepage():

    # Set number of games to retrieve
    num_games = 5

    # Get random games from the collection
    cursor = mongo.db.OpenSourceGames.aggregate([{ '$sample': { 'size': num_games } }])

    # Create a dictionary of the queried random games
    games_dict = {
        doc['name']: {
            'name': doc['name'],
            'display_name': doc['display_name'],
            'img_name': doc['img_name'],
            'url': doc['url'],
            'embed_link': doc['embed_link'],
            'date_added': doc['date_added']
        }
        for doc in cursor
    }

    os_grid = fill_grid_from_db(games_dict)
    free_game_grid = fill_grid()

    return render_template('homepage.html', grid_display=free_game_grid, os_grid=os_grid)



#Fetches highscores from pinball.js and adds them to the database
@app.route('/HighScores', methods=['POST'])
def highscores():
    highScores = request.json['highScores']
    result = highScores
    mongo.db.Highscores.insert_many(result)
    return jsonify({'result' : result})

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/2048')
def play_2048():
   return render_template('2048.html')


@app.route('/test/<string:tester>')
def test_get(tester):
    return tester


@app.route('/pinball')
def play_pinball():
    return render_template('pinball.html')


@app.route('/billiard')
def play_billard():
    return render_template('billiard.html')


@app.route('/multi-square')
def play_multi_square():
    return render_template('multiSquare.html')

@app.route('/chess')
def play_chess():
    return render_template('chess.html')

@app.route('/cannon-balls-3d')
def play_cannon_3D():
    return render_template('cannon3d.html')

@app.route('/checkers')
def play_checkers():
    return render_template('checkers.html')

@app.route('/table-tennis')
def play_tennis():
    return render_template('tableTennis.html')

@app.route('/bowling')
def play_bowling():
    return render_template('bowling.html')

@app.route('/archery-tour')
def play_archery():
    return render_template('archery.html')



#added to help aid in pulling from database by names
@app.route('/get_player_data', methods=['GET'])
def get_player_data():
    if request.method == 'GET':
        player_name = request.args.get('player_name')
        print(f"Searching for player: {player_name}")

        # Exclude _id field from the result
        player_data = mongo.db.HostedGames.find_one({'player_name': player_name}, {'_id': 0})

        if player_data:
            # Print player_data to the terminal
            print("Player Data:")
            for key, value in player_data.items():
                print(f"{key}: {value}")

            return jsonify(player_data)
        else:
            print("Player not found")
            return jsonify({'error': 'Player not found'}), 404



#added to help aid in pulling top 5 scores from database
@app.route('/get_top_5_scores', methods=['GET'])
def get_top_5_scores():
    if request.method == 'GET':
        # Sort by score in descending order and limit to 5
        top_5_scores = mongo.db.HostedGames.find(
            filter={},
            sort=[('score', -1)],
            projection={'_id': False},
            limit=5
        )

        if top_5_scores:
            # Print top 5 scores to the terminal
            print("Top 5 Scores:")
            for player_data in top_5_scores:
                for key, value in player_data.items():
                    print(f"{key}: {value}")
                print("---")

            return jsonify({'top_5_scores': list(top_5_scores)})
        else:
            print("No scores found")
            return jsonify({'error': 'No scores found'}), 404
        

# -----------------------DO NOT DELETE-----------------------
# DEV endpoint, should not be shipped with production
# @app.route('/add', methods=['GET', 'POST'])
# def add():

#   # Initialize form
#   form = GameForm(request.form)

#   # When information sent to server and required inputs are given
#   if request.method == 'POST' and form.validate():

#     # Add game to appropriate collection
#     if not(form.open_source.data):
#         mongo.db.FreeGames.insert_one({
#           'name': form.name.data,
#           'display_name': form.display_name.data,
#           'img_name': form.img_name.data,
#           'url': form.url.data,
#           'embed_link': form.embed_link.data,
#           'date_added': datetime.utcnow()
#         })
#     else:
#        mongo.db.OpenSourceGames.insert_one({
#           'name': form.name.data,
#           'display_name': form.display_name.data,
#           'img_name': form.img_name.data,
#           'url': form.url.data,
#           'embed_link': form.embed_link.data,
#           'date_added': datetime.utcnow()
#        })

#     # Create new entry
#     return redirect('add')

#   # Render empty form
#   elif request.method == 'GET':
#     return render_template('add.html', form=form)



# Dynamic route for rendering a specific game from the OpenSourceGames collection
@app.route('/OpenSourceGames/<name>', methods=['GET'])
def get_one_os_game(name):

    # Find document in collection by its 'name' field
    game_doc = mongo.db.OpenSourceGames.find_one({'name': name})

    # Create a dictionary from the queried document
    game_dict = {
        'name': game_doc['name'],
        'display_name': game_doc['display_name'],
        'img_name': game_doc['img_name'],
        'url': game_doc['url'],
        'embed_link': game_doc['embed_link'],
        'date_added': game_doc['date_added']
        }

    # Render html template file with queried game
    return render_template('open-source-game.html', game=game_dict)



# Simplified route that redirects to page one of open source games
@app.route('/OpenSourceGames', methods=['GET'])
def open_source_games():
    return redirect(url_for('get_all_os_games', page=1))



# Dynamic route for displaying paginated query of open source games in collection
@app.route('/OpenSourceGames/page/<int:page>', methods=['GET'])
def get_all_os_games(page):

    per_page = 9        # Number of games per page
    max_pages = 3       # Number of pages to show between first, last pages

    # Get the number of games in collection
    total_games = mongo.db.OpenSourceGames.count_documents({})

    # Calculate the total number of pages and start, end points
    total_pages = (total_games // per_page) + (1 if total_games % per_page > 0 else 0)
    start_page = max(1, page - max_pages // 2)
    end_page = min(total_pages, start_page + max_pages - 1)

    # Re-allign start_page
    start_page = max(1, end_page - max_pages + 1)

    # Get page range to display
    page_range = range(start_page, end_page + 1)

    # Get the game documents to display based on page
    cursor = mongo.db.OpenSourceGames.find().skip((page - 1) * per_page).limit(per_page)

    # Create a dictionary of the queried games
    games_dict = {
        doc['name']: {
            'name': doc['name'],
            'display_name': doc['display_name'],
            'img_name': doc['img_name'],
            'url': doc['url'],
            'embed_link': doc['embed_link'],
            'date_added': doc['date_added']
        }
        for doc in cursor
    }

    # Generate html string to create grid for the page
    game_grid = fill_grid_from_db(games_dict)

    return render_template('open-source-games.html', game_grid=game_grid, page=page, per_page=per_page,
                            total_games=total_games, total_pages=total_pages, page_range=page_range)

