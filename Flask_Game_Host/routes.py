#!/usr/bin/env python -B
import sys 
sys.dont_write_bytecode = True
from flask import Flask, render_template
from player import Player

app = Flask(__name__)

#temporary list of scores
top_players = [Player("Sam", 500), Player("Jeff", 2), Player("Sally", 1000), Player("Ryan", 50), Player("Lindsay", 750)]
#calling class method to sort scores
top_players = Player.sort_players(top_players)

def build_leaderboard_html():
  html_string = "<table class=\"leaderboard\"><tr><th>Username</th><th>Score</th></tr>"
  for obj in top_players:
    html_string += "<tr><td>" + obj.username + "</td>"
    html_string += "<td>" + str(obj.score) + "</td></tr>"
  html_string += "</table>"
  return html_string
  
  
  

@app.route('/')
def homepage():
  return render_template('homepage.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/game')
def game():
  leaderboard = build_leaderboard_html()
  return render_template('game.html', leaderboard_game1=leaderboard)

if __name__ == '__main__':
  app.run(debug=True)
