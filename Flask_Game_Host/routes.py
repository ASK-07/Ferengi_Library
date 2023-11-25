from Flask_Game_Host import app
from flask import render_template
from Flask_Game_Host.html_generator import fill_grid
from Flask_Game_Host.player import Player
from Flask_Game_Host.game import Game
import sys 
sys.dont_write_bytecode = True
from flask import jsonify, request, Blueprint
from .mongo_config import mongo

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

@app.route('/HighScores', methods=['POST'])
def highscores():
    highScores = request.json['highScores']
    result = highScores
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
        
        
@app.route('/OpenSourceGames/<game_name>')
def play_game(game_name):

    if game_name:
        return render_template(f'{game_name}.html')
    else:
        return 'Game not found', 404
