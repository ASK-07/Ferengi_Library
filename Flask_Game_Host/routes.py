'''
    This module defines the flask app's route decorators

'''
from Flask_Game_Host import app
from flask import render_template
from Flask_Game_Host.html_generator import fill_grid
from Flask_Game_Host.chess_engine import Engine
from Flask_Game_Host.player import Player
from Flask_Game_Host.game import Game



# <can be moved to html_generator once MongoDB API implemented>
#temporary list of scores
top_players = [Player("Sam", 500), Player("Jeff", 2), Player("Sally", 1000), Player("Ryan", 50), Player("Lindsay", 750)]
#temporary list of game titles to use for scoreboard
game_titles = [Game("Chess"), Game("Pinball")]
#calling class method to sort scores
top_players = Player.sort_players(top_players)

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


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/chess')
def chess():
  leaderboard = build_leaderboard_html()
  return render_template('chess.html', leaderboard_chess=leaderboard)


@app.route('/move/<int:depth>/<path:fen>/')
def get_move(depth, fen):
    print(depth)
    print("Calculating...")
    engine = Engine(fen)
    move = engine.iterative_deepening(depth - 1)
    print("Move found!", move)
    print()
    return move


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

@app.route('/chess1')
def play_chess():
    return render_template('chess1.html')


#@app.route('/save_high_scores', methods=['POST'])
#def save_high_scores():
    #score = request.form['score']
    #name = request.form['name']

    # Format the high score
   # high_score = f'{score} by {name}\n'

    # Save the high score to a text file
   # with open('high_scores.txt', 'a') as file:
     #   file.write(high_score)

   # return redirect('/')
   