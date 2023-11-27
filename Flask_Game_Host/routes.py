from Flask_Game_Host import app
from flask import redirect, render_template
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
    game_grid = fill_grid()
    return render_template('homepage.html', grid_display=game_grid)

#Fetches highscores from pinball.js and adds them to the database
@app.route('/HighScores', methods=['POST'])
def highscores():
    highScores = request.json['highScores']
    result = highScores
    mongo.db.Highscores.insert_many(result)
    return jsonify({'result' : result})


#Fetches best scores from local_storage_manager.js and adds them to the database
@app.route('/BestScores', methods=['POST'])
def handle_best_scores():
        data = request.get_json()
        new_score = data.get('newScore')

        mongo.db.Bestscores.insert_one(new_score)


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


@app.route('/1010-classic')
def play_1010():
    return render_template('1010.html')

@app.route('/daily-sudoku')
def play_sudoku():
    return render_template('dailySudoku.html')

@app.route('/chess')
def play_chess():
    return render_template('chess.html')

@app.route('/coloring-mandalas')
def play_coloring_mandalas():
    return render_template('coloringMandalas.html')

@app.route('/checkers')
def play_checkers():
    return render_template('checkers.html')

@app.route('/classic-solitaire')
def play_solitaire():
    return render_template('classicSolitaire.html')

@app.route('/bowling')
def play_bowling():
    return render_template('bowling.html')

@app.route('/alien-invaders2')
def play_alien_invaders2():
    return render_template('alienInvaders2.html')

@app.route('/mahjongg')
def play_mahjongg():
    return render_template('mahjongg.html')

@app.route('/ninja-darts')
def play_ninja_darts():
    return render_template('ninjaDarts.html')

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


@app.route('/OpenSourceGames/<name>', methods=['GET']) 
def get_one_os_game(name): 
 
    # Find document in collection by its 'name' field 
    game_doc = mongo.db.OpenSourceGames.find_one({'name': name}) 
 
    # Create a dictionary from the queried document 
    game_dict = { 
        'name': game_doc['name'], 
        'img_name': game_doc['img_name'], 
        'url': game_doc['url'], 
        'embed_link': game_doc['embed_link'], 
        'date_added': game_doc['date_added'] 
        } 
 
    # Render html template file with queried game 
    return render_template('open-source-game.html', game=game_dict)

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
        
# DEV endpoint, should not be shipped with production
@app.route('/add', methods=['GET', 'POST'])
def add():

  # Initialize form
  form = GameForm(request.form)

  # When information sent to server and required inputs are given
  if request.method == 'POST' and form.validate():

    # Add game to appropriate collection
    if not(form.open_source.data):
        mongo.db.FreeGames.insert_one({
          'name': form.name.data,
          'img_name': form.img_name.data,
          'url': form.url.data,
          'embed_link': form.embed_link.data,
          'date_added': datetime.utcnow()
        })
    else:
       mongo.db.OpenSourceGames.insert_one({
          'name': form.name.data,
          'img_name': form.img_name.data,
          'url': form.url.data,
          'embed_link': form.embed_link.data,
          'date_added': datetime.utcnow()
       })

    # Create new entry
    return redirect('add')

  # Render empty form
  elif request.method == 'GET':
    return render_template('add.html', form=form)

@app.route('/OpenSourceGames/page/<int:page>', methods=['GET']) 
def get_all_os_games(page): 
 
    # Set number of games to display per page 
    per_page = 9 
 
    # Get the number of games in collection 
    total_games = mongo.db.OpenSourceGames.count_documents({}) 
 
    # Get the game documents to display based on page 
    cursor = mongo.db.OpenSourceGames.find().skip((page - 1) * per_page).limit(per_page) 
 
    # Create a dictionary of the queried games 
    games_dict = { 
        doc['name']: { 
            'name': doc['name'], 
            'img_name': doc['img_name'], 
            'url': doc['url'], 
            'embed_link': doc['embed_link'], 
            'date_added': doc['date_added'] 
        } 
        for doc in cursor 
    } 
 
    # Generate html string to create grid for the page 
    game_grid = fill_grid_from_db(games_dict) 
 
    return render_template('open-source-games.html', game_grid=game_grid, page=page, per_page=per_page, total_games=total_games)