#!/usr/bin/env python -B
import sys 
sys.dont_write_bytecode = True
from flask import Flask, render_template
from chess_engine import Engine
from player import Player
from game import Game
from create_homepage_table import build_default_table

app = Flask(__name__, static_url_path='', static_folder='static',template_folder='templates')

#temporary list of scores
top_players = [Player("Sam", 500), Player("Jeff", 2), Player("Sally", 1000), Player("Ryan", 50), Player("Lindsay", 750)]
#temporary list of game titles to use for scoreboard
game_titles = [Game("Chess"), Game("Pinball")]
#calling class method to sort scores
top_players = Player.sort_players(top_players)

def build_leaderboard_html():
  html_string = "<table class=\"leaderboard\"><caption>" 
  html_string += game_titles[0].title + " Scoreboard</caption><tr><th>Username</th><th>Score</th></tr>"
  for obj in top_players:
    html_string += "<tr><td>" + obj.username + "</td>"
    html_string += "<td>" + str(obj.score) + "</td></tr>"
  html_string += "</table>"
  return html_string

@app.route('/')
def homepage():
  game_table = build_default_table()
  return render_template('homepage.html', game_display=game_table)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/game')
def game():
  leaderboard = build_leaderboard_html()
  return render_template('game.html', leaderboard_game1=leaderboard)

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


if __name__ == '__main__':
  app.run(debug=True)
